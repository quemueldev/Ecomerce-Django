from ..models import Order,OrderItem
from decimal import Decimal
from django.contrib.auth.models import User
from typing import Iterable
from cart.models import CartItem

class OrderOrm:
    def __init__(self):
        pass
    def remove_from_stock(self, product, quantity: int) -> None:
        product.stock -= quantity
        product.save(update_fields=['stock'])

    def finish_cart(self, cart):
        cart.status = 'finished'
        cart.save(update_fields=['status'])
    def build_order(self, user: User, price: Decimal) -> Order:
        #criar pedido
        order = Order.objects.create(
           user = user, total_price = price, status = 'created'
        )
        return order
    def build_orderItem(self, order: Order, items: Iterable[CartItem]) -> None:
        #copiar items para pedido
        OrderItem.objects.bulk_create([
        OrderItem(
            order=order,
            product=i.product,
            quantity=i.quantity,
            price_at_moment=i.price_at_moment
        )
        for i in items
        ])