from ..infra.orm import ProductsOrm
from ..utils.utils import ProductsUtils

class ProductService:
    def __init__(self, utils: ProductsUtils, orm: ProductsOrm):
        self.utils = utils
        self.orm = orm

    def list_category(self):
        categories = self.orm.get_category_queryset()
        return categories
    
    def list_product(self):
        products = self.orm.get_product_queryset()
        return products
    
    def create_category(self, user, data):
        print('chegou')
        self.utils.is_admin(user)
        print("verificou se e adm")
        self.orm.create_category(data)

    def delete_category(self, user,id):
        self.utils.is_admin(user)
        self.orm.delete_category(id)

    def create_product(self,user,data):
        self.utils.is_admin(user)
        self.orm.create_product(data)

    def delete_product(self,user,id):
        self.utils.is_admin(user)
        self.orm.delete_product(id)
    