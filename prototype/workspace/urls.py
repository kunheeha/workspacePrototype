from django.urls import path
from .views import DashboardListView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', DashboardListView.as_view(), name='user-dashboard'),
    path('workspace/<int:workspaceid>/', views.workspace, name='user-workspace'),
    path('workspace/<int:workspaceid>/<int:folderid>',
         views.folder, name='workspace-folder'),
    path('deletetodo/<int:workspaceid>/<int:todoid>', views.deleteTodo, name='delete-todo'),
]
