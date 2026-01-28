from ..services.services import ProductService
from ..utils.utils import ProductsUtils
from ..infra.orm import ProductsOrm



def build_product_service() -> ProductService:
    utils = ProductsUtils()
    orm = ProductsOrm()
    return ProductService(utils, orm)

