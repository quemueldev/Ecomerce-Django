from ninja import Router
from .schemas import *
from ninja_jwt.authentication import JWTAuth
from .infra.container import build_product_service
from .services.http import domain_errors
from core.infra.security import CookieJWTAuth


router_product = Router()

@router_product.get('category/', response=CategoryListSchema)
@domain_errors
def list_categories(request):
    service = build_product_service()
    categories = service.list_category()
    return {'retorno': 'sucesso', 'lista': list(categories)}
    
#admin only
@router_product.post('category/', auth=CookieJWTAuth()) #"e aqui"
@domain_errors
def create_categories(request, data:CreateCategorySchema):
    print(request.auth)
    service = build_product_service()
    service.create_category(request.auth, data) #erro aqui
    
    return {'retorno': 'sucesso'}
    
@router_product.delete('category/{id}', auth=JWTAuth)
@domain_errors
def delete_categories(request,id:int):
    service = build_product_service()
    service.delete_category(request.user, id)
    return {'retorno': 'sucesso'}
    
@router_product.get('product/', response=ProductListSchema)
@domain_errors
def list_products(request):
    service = build_product_service()
    products = service.list_product()
    return {'retorno': 'sucesso', 'lista': list(products)}

@router_product.post('product/', auth=CookieJWTAuth)
@domain_errors
def create_products(request, data:CreateProductSchema):
    service = build_product_service()
    service.create_product(request.user, data)
    return {'retorno': 'sucesso'}

@router_product.delete('product/{id}', auth=JWTAuth)
def delete_product(request,id:int):
    service = build_product_service()
    service.delete_product(request.user, id)
    return {'retorno': 'sucesso'}
    
    