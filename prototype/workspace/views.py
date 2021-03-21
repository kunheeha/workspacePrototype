from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView
from .models import Workspace, TodoItem, Folder


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


@login_required
def folder(request, *args, **kwargs):
    currentWorkspace = Workspace.objects.filter(
        id=kwargs['workspaceid']).first()
    currentFolder = Folder.objects.filter(id=kwargs['folderid']).first()
    authorised_users = User.objects.filter(workspace=currentWorkspace)

    context = {
        'workspace': currentWorkspace,
        'folder': currentFolder
    }
    if request.user in authorised_users:
        return render(request, 'workspace/folder.html', context)

    return render(request, 'workspace/deniedaccess.html')
