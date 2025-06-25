from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'priority', 'status', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o título da tarefa...',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Digite uma descrição detalhada...',
                'rows': 3
            }),
            'priority': forms.Select(attrs={
                'class': 'form-select'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'due_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            })
        }
        labels = {
            'title': 'Título',
            'description': 'Descrição',
            'priority': 'Prioridade',
            'status': 'Status',
            'due_date': 'Data de Vencimento'
        }
        help_texts = {
            'title': 'Digite um título claro e conciso para a tarefa.',
            'description': 'Opcional: Adicione detalhes sobre a tarefa.',
            'priority': 'Selecione a prioridade da tarefa.',
            'status': 'Selecione o status atual da tarefa.',
            'due_date': 'Opcional: Defina uma data de vencimento.'
        }

class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'priority', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'priority': forms.Select(attrs={
                'class': 'form-select'
            }),
            'due_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            })
        }
        labels = {
            'title': 'Título',
            'description': 'Descrição',
            'priority': 'Prioridade',
            'due_date': 'Data de Vencimento'
        }
