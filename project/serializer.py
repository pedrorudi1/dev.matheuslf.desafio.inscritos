from rest_framework import serializers
from .models import Projects

class ProjectSerializer(serializers.ModelSerializer):
    modelProjects = Projects
    fieldsProject = '__all__'