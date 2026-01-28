from ninja.errors import HttpError
from products.models import Product
from ..models import CartItem
from decimal import Decimal
from ..services.errors import *

class CartUtils:
    def __init__(self):
        pass

    def validate_stock(self, product, quantity):
        if product.stock < quantity:
            raise StockError()

    def calculate_subtotal(self, item):
        calc = item.product.price * item.quantity
        return calc

    def serialize_item(self, item, subtotal):
        return {
            'product_id': item.product.id,
            'name': item.product.name,
            'price': item.product.price,
            'quantity': item.quantity,
            'subtotal': subtotal
        }

