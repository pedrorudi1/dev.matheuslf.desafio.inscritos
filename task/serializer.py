from rest_framework import serializers
from .models import Tasks

class TasksSerializer(serializers.ModelSerializer):

    modelTasks = Tasks
    fieldsTasks = ('title', 'description', 'status', 'priority', 'dueDate')