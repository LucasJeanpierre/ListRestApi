from django.contrib import admin
from .models import ShoppingList

class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'bougth')

# Register your models here.

admin.site.register(ShoppingList, ShoppingListAdmin)