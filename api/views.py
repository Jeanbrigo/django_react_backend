from django.shortcuts import render
from api.models import Todo
from api.serializers import TodoSerializer
from rest_framework.viewsets import ModelViewSet


class TodoViews(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer