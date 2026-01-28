class DomainCartError:
    pass
class StockError(DomainCartError):
    pass
class ProductNotExist(DomainCartError):
    pass
class ItemNotInCart(DomainCartError):
    pass