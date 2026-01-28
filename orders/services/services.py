from .errors import *
from ..infra.orm import OrderOrm
from ..utils.utils import OrderUtils
from cart.providers.container import build_cart_service
from django.db import transaction


"""
chekout
1. Busca carrinho open do usuário //x
2. Valida:
   - carrinho existe
   - carrinho tem itens //x
3. Calcula total (regra de domínio) // x
4. Cria pedido //x
5. Copia itens do carrinho → itens do pedido //x
6. Finaliza carrinho (status = finished) //x
"""
class OrderService:
    def __init__(self, utils: OrderUtils, orm: OrderOrm):
        self.utils = utils
        self.orm = orm

    @transaction.atomic
    def create_order(self, user):
        service = build_cart_service(user)
        cart = service.get_or_create_open_cart()
        items = list(cart.items.select_related('product'))

        self.utils.check_cart_items(items)
        self.utils.validate_stock(items)

        total = self.utils.calculate_total(items)

        order = self.orm.build_order(
            user= user, price= total
        )

        self.orm.build_orderItem(
            order, items
        )
        
        for i in items:
            self.orm.remove_from_stock(i.product, i.quantity)

        self.orm.finish_cart(cart)

        
