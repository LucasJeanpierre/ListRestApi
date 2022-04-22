from django.db import models

# Create your models here.

class ShoppingList(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    bougth = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name
