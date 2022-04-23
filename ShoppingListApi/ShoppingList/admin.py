from django.contrib import admin
from .models import ShoppingList, ShoppingItem

class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ['name']

class ShoppingItemAdmin(admin.ModelAdmin):
    list_display =  ['name', 'quantity', 'bougth']


# Register your models here.

admin.site.register(ShoppingList, ShoppingListAdmin)
admin.site.register(ShoppingItem, ShoppingItemAdmin)