from rest_framework import viewsets
from tarefas_app import models
from .serializers import TaskSerializer, CategorySerializer, PrioritySerializer
from rest_framework import permissions

class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class PriorityViewSet(viewsets.ModelViewSet):
    queryset = models.Priority.objects.all()
    serializer_class = PrioritySerializer
    permission_classes = [permissions.IsAuthenticated]