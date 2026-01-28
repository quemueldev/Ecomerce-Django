from ..services.erros import *
from ..models import Category, Product


class ProductsOrm:
    def __init__(self):
        self.a = '1'

    def get_category_queryset(self):
        list = Category.objects.all().values(
            'id',
            'name'
        )
        return list
        
    def get_product_queryset(self) -> dict:
        list = Product.objects.all().values(
            'name',
            'stock', 
            'category',
            'price',
            'is_active'
        )
        return list
    def create_category(self,data):
        category = Category.objects.create(
            name=data.name
        )
    def delete_category(self, id):
        try:
            obj = Category.objects.get(id = id).delete()
        except Category.DoesNotExist:
            raise CategoryDoesNotExist()
        
    def create_product(self,data):
        try:
            category = Category.objects.get(id = data.category_id)
        except Category.DoesNotExist:
            raise CategoryDoesNotExist()
        
        product = Product.objects.create(
            name=data.name,
            stock=data.stock,
            category=category,
            price=data.price,
            is_active=data.is_active
        )
    def delete_product(self):
        try:
            obj = Product.objects.get(id = id).delete()
        except Product.DoesNotExist:
            raise ProductDoesNotExist()

        
        