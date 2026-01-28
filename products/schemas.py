from ninja import Schema
from typing import List

class ProductSchema(Schema):
    name:str
    stock:int
    category:str
    price:float
    is_active:bool
class ProductListSchema(Schema):
    retorno:str
    lista: List[ProductSchema]


class CategorySchema(Schema):
    id:int
    name:str
class CategoryListSchema(Schema):
    retorno: str
    lista: List[CategorySchema]


class CreateProductSchema(Schema):
    name:str
    stock:int
    category_id:int
    price:float
    is_active:bool

class CreateCategorySchema(Schema):
    name:str
