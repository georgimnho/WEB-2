from rest_framework import viewsets
from tarefas_app import models
from .serializers import TaskSerializer, CategorySerializer, PrioritySerializer
from rest_framework import permissions
import logging
logger = logging.getLogger('custom')


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        logger.info(f'Tarefa criada: {response.data["title"]} - Categoria: {response.data["category_name"]} - Prioridade: {response.data["priority_level"]}')
        return response

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        logger.info(f'Categoria criada: {response.data["name"]}')
        return response


class PriorityViewSet(viewsets.ModelViewSet):
    queryset = models.Priority.objects.all()
    serializer_class = PrioritySerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        logger.info(f'Prioridade criada: {response.data["level"]}')
        return response