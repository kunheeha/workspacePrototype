from django.urls import path
from .views import DashboardListView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', DashboardListView.as_view(), name='user-dashboard'),
]
