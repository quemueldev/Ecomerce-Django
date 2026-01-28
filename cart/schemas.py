from ninja import Schema
from typing import List
from decimal import Decimal

class CartSchema(Schema):
    id: int
    quantity: int = 1

class CartItemSchema(Schema):
    product_id: int
    name: str
    price: Decimal
    quantity: int
    subtotal: Decimal

class GetCartSchema(Schema):
    retorno: str
    cart_id: int
    items: List[CartItemSchema]
    total: Decimal

