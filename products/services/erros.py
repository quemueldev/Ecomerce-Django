class DomainProductError:
    pass

class NotPermissionError(DomainProductError):
    pass

class InternalError(DomainProductError):
    pass

class CategoryDoesNotExist(DomainProductError):
    pass
class ProductDoesNotExist(DomainProductError):
    pass