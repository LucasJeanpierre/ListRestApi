from asyncio.windows_events import NULL
from unicodedata import name
from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .serializer import ShoppingListSerializer, ShoppingItemSerializer
from .models import ShoppingList, ShoppingItem
from .permissions import IsAdminAuthenticated, IsUserAuthenticated, IsUserInCorrectGroup

from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ShoppingItemView(viewsets.ModelViewSet):

    def get_shopping_id(self):
        shoppinglist_name = self.request.GET.get('shoppinglist')
        if shoppinglist_name is not None:
            shoppinglist=ShoppingList.objects.filter(name=shoppinglist_name)
            if shoppinglist.exists():
                return shoppinglist.first().id
        return None

     
    permission_classes = [IsUserInCorrectGroup | IsAdminAuthenticated]

    def get_permissions(self):
        shoppinglist_name = self.request.GET.get('shoppinglist')
        if shoppinglist_name is not None:
            return [permission(shoppinglist_name) for permission in self.permission_classes]
        return super().get_permissions()
    
    
    #queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer

    def get_queryset(self):
        queryset = ShoppingItem.objects.all()
        shoppinglist_id = self.get_shopping_id()
        if shoppinglist_id is not None:
            queryset = queryset.filter(shoppinglist=shoppinglist_id)

        return queryset

class ShoppingListView(viewsets.ModelViewSet):

    
    permission_classes = [IsAdminAuthenticated]

    queryset = ShoppingList.objects.all()  
    serializer_class = ShoppingListSerializer

    def get_permissions(self):
        print(self.queryset)
        return super().get_permissions()