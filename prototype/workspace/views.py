from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from .models import Workspace, TodoItem, Folder, Notebook, Note


def home(request):
    return render(request, 'workspace/home.html')


class DashboardListView(LoginRequiredMixin, ListView):
    model = Workspace
    template_name = 'workspace/dashboard.html'
    context_object_name = 'workspaces'

    def get_queryset(self):
        dashuser = self.request.user
        return Workspace.objects.filter(users=dashuser)


@login_required
def workspace(request, *args, **kwargs):
    workspaceid = kwargs['workspaceid']
    currentWorkspace = Workspace.objects.filter(id=workspaceid).first()
    todoitems = TodoItem.objects.filter(workspace=currentWorkspace)
    folders = Folder.objects.filter(workspace=currentWorkspace)
    authorised_users = User.objects.filter(workspace=currentWorkspace)

    context = {
        'workspace': currentWorkspace,
        'todoitems': todoitems,
        'folders': folders
    }

    if request.method == 'POST':
        if 'addTodo' in request.POST:
            name = request.POST['todoName']
            newTodo = TodoItem(name=name, workspace=currentWorkspace)
            newTodo.save()
            return redirect('user-workspace', workspaceid=workspaceid)

    if request.user in authorised_users:
        return render(request, 'workspace/workspace.html', context)

    return render(request, 'workspace/deniedaccess.html')


def deleteTodo(request, *args, **kwargs):
    workspaceid = kwargs['workspaceid']
    todoId = kwargs['todoid']
    todoitem = TodoItem.objects.filter(id=todoId).first()
    todoitem.delete()
    return redirect('user-workspace', workspaceid=workspaceid)


def markTodo(request, *args, **kwargs):
    workspaceid = kwargs['workspaceid']
    todoId = kwargs['todoid']
    todoitem = TodoItem.objects.filter(id=todoId).first()
    if todoitem.complete:
        todoitem.complete = False
    elif not todoitem.complete:
        todoitem.complete = True
    todoitem.save()
    return redirect('user-workspace', workspaceid=workspaceid)


@login_required
def folder(request, *args, **kwargs):
    currentWorkspace = Workspace.objects.filter(
        id=kwargs['workspaceid']).first()
    currentFolder = Folder.objects.filter(id=kwargs['folderid']).first()
    notebooks = Notebook.objects.filter(folder=currentFolder)
    authorised_users = User.objects.filter(workspace=currentWorkspace)

    context = {
        'workspace': currentWorkspace,
        'folder': currentFolder,
        'notebooks': notebooks
    }
    if request.user in authorised_users:
        return render(request, 'workspace/folder.html', context)

    return render(request, 'workspace/deniedaccess.html')


def notebookView(request, *args, **kwargs):
    workspaceid = kwargs['workspaceid']
    notebookid = kwargs['notebookid']
    currentWorkspace = Workspace.objects.filter(id=workspaceid).first()
    currentNotebook = Notebook.objects.filter(id=notebookid).first()
    authorised_users = User.objects.filter(workspace=currentWorkspace)
    notes = Note.objects.filter(notebook=currentNotebook)
    context = {
        'workspace': currentWorkspace,
        'currentnotebook': currentNotebook,
        'notes': notes
    }

    if request.user in authorised_users:
        return render(request, 'workspace/notebook.html', context)

    return render(request, 'workspace/deniedaccess.html')


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.notebook = Notebook.objects.filter(
            id=self.kwargs['notebookid']).first()
        return super().form_valid(form)


class NoteEditView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.notebook = Notebook.objects.filter(
            id=self.kwargs['notebookid']).first()
        return super().form_valid(form)
