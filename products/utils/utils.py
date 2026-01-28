from ..services.erros import *
from ..models import Category, Product


class ProductsUtils:
    def __init__(self):
        self.a = '1'

    def is_admin(self, user):
        if not user[0].is_superuser: # user -> tuple
            raise NotPermissionError()

    