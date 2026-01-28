from .erros import *
from ninja.errors import HttpError


DOMAIN_ERROR_MAP = {
    InvalidEmailError: (400, "Email inválido"),
    EmailAlreadyInUseError: (400, "Email já em uso"),
    EmailSendError: (500, "Erro ao enviar email"),
    CodeDoesntExist: (400, "Código inválido"),
    ExpiredCode: (403, "Código expirado"),
    MinValueNameError: (400, "Seu nome deve ter no mínimo 3 caracteres"),
    MinValuePasswordError: (400, "Sua senha deve ter no mínimo 6 dígitos"),
    EmailDiferentForToken: (400, "Email não correspondente ao token"),
    NotPermitedToRegister: (403, "Você não tem permissão para se cadastrar"),
    UserIsNoneError: (401, "Usuário não encontrado"),
    InternalError: (500, "Erro interno"),
}

def handle_error(exc: DomainError):
    status, message = DOMAIN_ERROR_MAP.get(type(exc), (500, "Erro interno"))
    raise HttpError(status, message)
from functools import wraps

def domain_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DomainError as e:
            handle_error(e)
    return wrapper
