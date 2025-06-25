# todolist/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 1) Painel Admin em /admin/
    path('admin/', admin.site.urls),

    # 2) Seu app de tarefas como página principal
    path('', include('tasks.urls')),
]
