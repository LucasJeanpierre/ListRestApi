from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ShoppingListSerializer, ShoppingItemSerializer
from .models import ShoppingList, ShoppingItem

from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ShoppingItemView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]

    queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer

class ShoppingListView(viewsets.ModelViewSet):

    #permission_classes = [IsAuthenticated]

    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer