from ..services.errors import *

class OrderUtils:
    def __init__(self):
        pass

    def check_cart_items(self, items):
        if not items:
            raise EmpityCartError()
        
    def validate_stock(self, items):
        for i in items:
            if i.product.stock < i.quantity:
                raise StockError(i.product.name)
    
    def calculate_total(self, items):
        a = 1