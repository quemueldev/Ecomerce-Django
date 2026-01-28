from ninja import NinjaAPI
from core.routers import router_core 
from users.router import auth
from products.router import router_product
from cart.router import router_cart
from orders.router import router_order

nucleo = NinjaAPI(
    title='E-comerce API',
    openapi_url='api'
)
nucleo.add_router('core', router_core)
nucleo.add_router('auth', auth)
nucleo.add_router('products', router_product)
nucleo.add_router('carts', router_cart)
nucleo.add_router('orders', router_order)