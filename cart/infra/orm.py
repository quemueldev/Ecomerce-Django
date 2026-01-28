from django.core.exceptions import MultipleObjectsReturned
from ..models import Cart,CartItem
from ..services.errors import *
from products.models import Product

class CartOrm:
    def __init__(self, user):
        self.user = user
    def get_open_carts(self):
        return Cart.objects.filter(user=self.user, status='open')

    def create_open_cart(self):
        return Cart.objects.create(user=self.user, status='open')

    def finish_carts(self, carts):
        carts.update(status='finished')

    def create_cartItem(self,cart, product, quantity):
        CartItem.objects.create(
            cart=cart,
            product=product,
            quantity=quantity,
            price_at_moment=product.price
        )
    def update_quantity(self, item, quantity, product):
        item.quantity = quantity
        item.save()

    def get_product(self, product_id):
        try:
            return Product.objects.get(id=product_id, is_active=True)
        except Product.DoesNotExist:
            raise ProductNotExist()

    def get_cartItem(self,cart, product):
        try:
            return CartItem.objects.get(cart=cart, product=product)
        except CartItem.DoesNotExist:
            return None
    def remove_item(self,cart, id):
        try:
            item = CartItem.objects.get(cart=cart, product_id=id).delete()
        except CartItem.DoesNotExist:
            raise ItemNotInCart()
