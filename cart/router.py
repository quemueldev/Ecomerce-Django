from ninja import Router
from ninja.errors import HttpError
from ninja_jwt.authentication import JWTAuth
from decimal import Decimal


from .models import Cart,CartItem
from products.models import Product
from .schemas import CartSchema,GetCartSchema
from .providers.container import build_cart_service
from .services.http import domain_errors

router_cart = Router()

@router_cart.get(
    'cart/',
    auth=JWTAuth,
    response=GetCartSchema,
    tags=['cart']
    )
@domain_errors
def list_cart(request):
    service = build_cart_service(request.user)
    items, total_price = service.get_items_and_price_of_cart()

    return {
        'retorno': 'sucesso',
        'items': items,
        'total': total_price
    }


@router_cart.post(
    'cart/',
    auth=JWTAuth,
    response=dict,
    tags=['cart']
    )
@domain_errors
def add_to_cart(request, data:CartSchema):
    service = build_cart_service(request.user)
    service.add_product_to_cart(
        request.user,
        data.id,
        data.quantity
    )
    
    return {'retorno': 'sucesso'}


@router_cart.delete(
    'cart/{id}',
    auth=JWTAuth,
    )
@domain_errors
def remove_from_cart(request,id: int):
    service = build_cart_service(request.user)
    service.remove_from_cart(id)

    return {'retorno': 'sucesso'}


