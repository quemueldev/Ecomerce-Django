from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    name= models.CharField(
        max_length=155, 
        unique=True
    )
    def __str__(self):
        return self.name

class Product(models.Model):
    # o admin quando eu criar
    name = models.CharField(max_length=70)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2, 
        validators=[MinValueValidator(1)]
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



    