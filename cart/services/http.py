from .errors import *
from ninja.errors import HttpError


DOMAIN_ERROR_MAP = {
    StockError: HttpError(403, 'estoque insuficiente'),
    
}

def handle_error(exc: DomainCartError):
    status, message = DOMAIN_ERROR_MAP.get(type(exc), (500, "Erro interno"))
    raise HttpError(status, message)
from functools import wraps

def domain_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DomainCartError as e:
            handle_error(e)
    return wrapper
