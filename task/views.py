from rest_framework import generics
from .models import Tasks
from .serializer import TasksSerializer
# Create your views here.

class TasksList(generics.ListCreateAPIView):

    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer