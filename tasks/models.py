from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone
from datetime import datetime

class Todo(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Baixa'),
        ('medium', 'Média'),
        ('high', 'Alta'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('in_progress', 'Em Progresso'),
        ('completed', 'Concluída'),
        ('cancelled', 'Cancelada'),
    ]
    
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(3, "O título deve ter pelo menos 3 caracteres.")],
        verbose_name="Título"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descrição"
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name="Concluída"
    )
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium',
        verbose_name="Prioridade"
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="Status"
    )
    due_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Data de Vencimento"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de Criação"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Data de Atualização"
    )
    completed_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Data de Conclusão"
    )

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['is_completed']),
            models.Index(fields=['priority']),
            models.Index(fields=['status']),
            models.Index(fields=['due_date']),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Atualiza a data de conclusão quando a tarefa é marcada como concluída
        if self.is_completed and not self.completed_at:
            self.completed_at = timezone.now()
        elif not self.is_completed:
            self.completed_at = None
        super().save(*args, **kwargs)

    @property
    def is_overdue(self):
        """Verifica se a tarefa está atrasada"""
        if self.due_date and not self.is_completed:
            return timezone.now() > self.due_date
        return False

    @property
    def days_until_due(self):
        """Retorna o número de dias até o vencimento"""
        if self.due_date and not self.is_completed:
            now = timezone.now()
            if self.due_date > now:
                delta = self.due_date - now
                return delta.days
            else:
                return 0
        return None

    def mark_as_completed(self):
        """Marca a tarefa como concluída"""
        self.is_completed = True
        self.status = 'completed'
        self.completed_at = timezone.now()
        self.save()

    def mark_as_in_progress(self):
        """Marca a tarefa como em progresso"""
        self.status = 'in_progress'
        self.save()

    def cancel_task(self):
        """Cancela a tarefa"""
        self.status = 'cancelled'
        self.save()

    def get_priority_color(self):
        """Retorna a cor CSS baseada na prioridade"""
        colors = {
            'low': 'text-success',
            'medium': 'text-warning',
            'high': 'text-danger',
        }
        return colors.get(str(self.priority), 'text-secondary')

    def get_status_color(self):
        """Retorna a cor CSS baseada no status"""
        colors = {
            'pending': 'text-secondary',
            'in_progress': 'text-primary',
            'completed': 'text-success',
            'cancelled': 'text-danger',
        }
        return colors.get(str(self.status), 'text-secondary')
