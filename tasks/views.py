from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm, TodoCreateForm

def home(request):
    """View principal que exibe todas as tarefas e permite criar novas"""
    if request.method == 'POST':
        # Toggle de conclusão (não é o formulário principal)
        if 'toggle_id' in request.POST:
            todo = get_object_or_404(Todo, pk=request.POST['toggle_id'])
            todo.is_completed = not todo.is_completed
            if todo.is_completed:
                todo.mark_as_completed()
            else:
                todo.status = 'pending'
                todo.completed_at = None
            todo.save()
            return redirect('home')

        # Criação de nova tarefa
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa criada com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro ao criar tarefa. Verifique os dados e tente novamente.')
    else:
        form = TodoCreateForm()

    # Buscar tarefas organizadas por status
    pending = Todo.objects.filter(is_completed=False).order_by('-created_at')
    completed = Todo.objects.filter(is_completed=True).order_by('-created_at')
    
    return render(request, 'home.html', {
        'form': form,
        'pending': pending,
        'completed': completed,
    })

def edit(request, pk):
    """View para editar uma tarefa existente"""
    todo = get_object_or_404(Todo, pk=pk)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro ao atualizar tarefa. Verifique os dados.')
    else:
        form = TodoForm(instance=todo)
    
    return render(request, 'edit.html', {
        'form': form,
        'todo': todo,
    })

def delete(request, pk):
    """View para deletar uma tarefa"""
    todo = get_object_or_404(Todo, pk=pk)
    
    if request.method == 'POST':
        todo_title = todo.title
        todo.delete()
        messages.success(request, f'Tarefa "{todo_title}" excluída com sucesso!')
        return redirect('home')
    
    return render(request, 'delete.html', {
        'todo': todo,
    })

@require_POST
def toggle_status(request, pk):
    """View para alternar o status de uma tarefa via AJAX"""
    try:
        todo = get_object_or_404(Todo, pk=pk)
        if request.POST.get('action') == 'complete':
            todo.mark_as_completed()
        elif request.POST.get('action') == 'in_progress':
            todo.mark_as_in_progress()
        elif request.POST.get('action') == 'cancel':
            todo.cancel_task()
        else:
            # Toggle simples
            todo.is_completed = not todo.is_completed
            if todo.is_completed:
                todo.mark_as_completed()
            else:
                todo.status = 'pending'
                todo.completed_at = None
            todo.save()
        
        return JsonResponse({
            'success': True,
            'is_completed': todo.is_completed,
            'status': todo.status,
            'status_display': todo.get_status_display()
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })

def about(request):
    """View para a página sobre o projeto"""
    return render(request, 'about.html')
