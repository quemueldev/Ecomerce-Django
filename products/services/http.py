from .erros import *
from ninja.errors import HttpError


DOMAIN_ERROR_MAP = {
    NotPermissionError: (403, "Permissão negada"),
    InternalError: (500, "Erro interno"),
    CategoryDoesNotExist: (404, "Categoria não encontrada"),
    ProductDoesNotExist: (404, "Produto não encontrado"),
}

def handle_error(exc):
    status, message = DOMAIN_ERROR_MAP.get(type(exc), (500, "Erro interno"))
    raise HttpError(status, message) from exc
from functools import wraps

def domain_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DomainProductError as e:
            handle_error(e)
    return wrapper
