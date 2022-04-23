from rest_framework import serializers
from .models import ShoppingList, ShoppingItem

class ShoppingListSerializer(serializers.ModelSerializer):

    items = serializers.SerializerMethodField()
    class Meta:
        model = ShoppingList
        fields = ('id', 'name', 'items')

    def get_items(self, instance):
        queryset = ShoppingItem.objects.filter(shoppinglist=instance)
        serializer = ShoppingItemSerializer(queryset, many=True)
        return serializer.data


class ShoppingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingItem
        fields = ('id', 'name', 'quantity', 'bougth')