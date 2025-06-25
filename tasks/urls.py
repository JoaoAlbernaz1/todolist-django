# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',               views.home,   name='home'),    # GET /tasks/
    path('edit/<int:pk>/', views.edit,   name='edit'),    # GET /tasks/edit/1/
    path('delete/<int:pk>/', views.delete, name='delete'),# GET /tasks/delete/1/
    path('toggle-status/<int:pk>/', views.toggle_status, name='toggle_status'),
    path('about/', views.about, name='about'),
]
