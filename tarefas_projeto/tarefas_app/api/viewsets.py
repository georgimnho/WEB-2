from rest_framework import viewsets
from tarefas_app import models
from .serializers import TaskSerializer, CategorySerializer, PrioritySerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer

class PriorityViewSet(viewsets.ModelViewSet):
    queryset = models.Priority.objects.all()
    serializer_class = PrioritySerializer