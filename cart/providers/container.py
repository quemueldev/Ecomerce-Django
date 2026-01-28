from ..utils.utils import CartUtils
from ..infra.orm import CartOrm
from ..services.services import CartService

def build_cart_service(user):
    utils = CartUtils()
    orm = CartOrm(user)
    return CartService(utils, orm)