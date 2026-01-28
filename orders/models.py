from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart
from products.models import Product
from django.core.validators import MinValueValidator

ORDER_STATUS = [
    ('created', 'Criado'),
    ('paid', 'Pago'),
    ('shipped', 'Enviado'),
    ('delivered', 'Entregue'),
    ('canceled', 'Cancelado'),
]

class Order(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.PROTECT, 
        related_name='order'
    )
    total_price = models.DecimalField(
        max_digits=8, 
        decimal_places=2,
    )
    status = models.CharField(
        max_length=80, 
        choices=ORDER_STATUS,
        default='created'
        )
    created_at = models.DateField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price_at_moment = models.DecimalField(
        max_digits=8, 
        decimal_places=2,
    )
    
    class Meta:
        unique_together = ('order', 'product')