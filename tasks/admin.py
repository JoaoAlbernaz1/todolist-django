from django.contrib import admin
from .models import Todo

# Faz o "View site" apontar para /
admin.site.site_url = '/'

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_completed', 'priority', 'status', 'due_date', 'created_at')
    list_filter = ('is_completed', 'priority', 'status', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    list_editable = ('priority', 'status', 'is_completed')
    readonly_fields = ('created_at', 'updated_at', 'completed_at')
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'description')
        }),
        ('Status e Prioridade', {
            'fields': ('is_completed', 'status', 'priority')
        }),
        ('Datas', {
            'fields': ('due_date', 'created_at', 'updated_at', 'completed_at'),
            'classes': ('collapse',)
        }),
    )
