from ..models import Cart
from django.core.exceptions import MultipleObjectsReturned
from decimal import Decimal
from ..utils.utils import CartUtils
from ..infra.orm import CartOrm


class CartService:
    def __init__(self, utils: CartUtils, orm: CartOrm):
        self.utils = utils
        self.orm = orm

    def get_or_create_open_cart(self):
        cart_queryset = self.orm.get_open_carts()

        if not cart_queryset.exists():
            cart = self.orm.create_open_cart()
            return cart
        
        if cart_queryset.count() == 1:
            return cart_queryset.first()
        else:
            cart = cart_queryset.order_by('-created_at').first()
            self.orm.finish_carts(cart_queryset.exclude(id=cart.id))
            return cart

    def get_items_and_price_of_cart(self):
        cart = self.get_or_create_open_cart()
        items_list = []
        total = Decimal('0')
        items = cart.items.select_related('product')

        for i in items:
            subtotal = self.utils.calculate_subtotal(i) # preço X quantidade
            total += subtotal

            items_list.append(self.utils.serialize_item(i, subtotal))

        return items_list, total

    def add_product_to_cart(self, id, quantity):
        cart = self.get_or_create_open_cart()
        product = self.orm.get_product(id)

        item = self.orm.get_cartItem(cart, product)

        new_quantity = quantity
        if item:
            new_quantity += item.quantity
        self.utils.validate_stock(product, new_quantity)

        if item:
            self.orm.update_quantity(item, new_quantity)
        else:
            self.orm.create_cartItem(cart, product, quantity)
    def remove_from_cart(self,id):
        cart = self.get_or_create_open_cart()
        self.orm.remove_item(id)

