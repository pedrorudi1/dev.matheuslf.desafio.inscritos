from django.db import models
from project.models import Projects

# Create your models here.
class Tasks(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=150)
    description = models.CharField("Detalhes da Tarefa")
    status_choice = models.TextChoices("status_choices", "TODO DOING DONE")
    status = models.CharField(choices=status_choice)
    priority_choice = models.TextChoices("priority_choices", "LOW MEDIUM HIGH")
    priority = models.CharField(choices=priority_choice)
    dueDate = models.DateField()
    projectId = models.ForeignKey(Projects, on_delete=models.PROTECT)

    def __str__(self):
        return self.title