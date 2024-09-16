from rest_framework import serializers
from tarefas_app import models
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = '__all__' 


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__' 


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Priority
        fields = '__all__' 