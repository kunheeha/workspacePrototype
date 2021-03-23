from django.urls import path
from .views import DashboardListView, NoteCreateView, NoteEditView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', DashboardListView.as_view(), name='user-dashboard'),
    path('workspace/<int:workspaceid>/', views.workspace, name='user-workspace'),
    path('workspace/<int:workspaceid>/<int:folderid>/',
         views.folder, name='workspace-folder'),
    path('deletetodo/<int:workspaceid>/<int:todoid>/',
         views.deleteTodo, name='delete-todo'),
    path('marktodo/<int:workspaceid>/<int:todoid>/',
         views.markTodo, name='mark-todo'),
    path('notebook/<int:workspaceid>/<int:notebookid>/',
         views.notebookView, name='notebook'),
    path('notebook/<int:notebookid>/newnote/',
         NoteCreateView.as_view(), name='new-note'),
    path('notebook/<int:notebookid>/<int:pk>/editnote/',
         NoteEditView.as_view(), name='edit-note'),
    path('workspace/<int:workspaceid>/<int:folderid>/<int:fileid>/delete/',
         views.delete_file, name='delete-file'),
]
