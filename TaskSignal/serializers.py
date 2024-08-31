from rest_framework import serializers
from .models import Task, SubTask

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # Сделать поле только для чтения

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'owner', 'created_at', 'updated_at']

class SubTaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # Сделать поле только для чтения

    class Meta:
        model = SubTask
        fields = ['id', 'task', 'title', 'owner', 'created_at', 'updated_at']