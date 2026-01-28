class DomainError(Exception):
    """Erro base do domínio"""
    pass

class InvalidEmailError(DomainError):
    pass
class EmailAlreadyInUseError(DomainError):
    pass
class EmailSendError(DomainError):
    pass
class CodeDoesntExist(DomainError):
    pass
class ExpiredCode(DomainError):
    pass
class MinValueNameError(DomainError):
    pass
class MinValuePasswordError(DomainError):
    pass
class EmailDiferentForToken(DomainError):
    pass
class NotPermitedToRegister(DomainError):
    pass
class UserIsNoneError(DomainError):
    pass
class InternalError(DomainError):
    pass