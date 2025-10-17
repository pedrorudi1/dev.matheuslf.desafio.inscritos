from rest_framework import generics
from .models import Projects
from .serializer import ProjectSerializer

# Create your views here.
class ProjectsList(generics.ListCreateAPIView):
    
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer