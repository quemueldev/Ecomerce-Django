class DomainOrderError:
    pass
class EmpityCartError(DomainOrderError):
    pass
class StockError(DomainOrderError):
    def __init__(self, product_name):
        super().__init__(f'Estoque insuficiente para {product_name}')