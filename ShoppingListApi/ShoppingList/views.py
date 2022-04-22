from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ShoppingListSerializer
from .models import ShoppingList

# Create your views here.

class ShoppingListView(viewsets.ModelViewSet):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer