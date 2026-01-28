from ..schemas import EmailSchema
import random
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from ninja.errors import HttpError
from ..models import VerificationCode
import jwt
from ..utils.utils import EmailUtils
from ..infra.orm import EmailOrm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import timezone
from django.db import IntegrityError
from ..infra.gateway import EmailSender

from datetime import timedelta

EMAIL = settings.EMAIL_HOST_USER
CHAVE = settings.SECRET_KEY

class EmailService:
    def __init__(self, utils:EmailUtils, orm: EmailOrm, sender: EmailSender):
        self.utils = utils
        self.orm = orm
        self.sender = sender
    #codigo de verificação
    def send_code(self) -> None:
        self.utils.validate_email()
        code_gerated = self.utils.generate_code()
        code = self.orm.code_to_db(code_gerated)
        self.sender.send_email(self.utils.email,code)

    def verify_code(self,code:str) -> dict:
        self.orm.verify(code)
        payload = self.utils.generate_payload()
        return payload
    
    def register(self, data, token) -> User:
        self.utils.validate_email()
        self.orm.validate_is_unique()
        payload = get_payload(token)
        self.utils.validate_payload(payload)
        self.utils.validate_len_data(data)

        user = self.orm.create_user(data)
        return user
    def authenticate_user(self, password: str) -> User:
        user = self.utils.validate_user(password)
        return user
    
    def serialize_user(self, user: User) -> dict:
        user_fields = self.utils.serialize_user(user)
        return user_fields
    
    def set_cookies(self, response, access, refresh, csrf):
        response.set_cookie(
            key='access',
            value=access,
            httponly=True,
            samesite='lax',
            secure=False,
        )
        response.set_cookie(
            key='refresh',
            value=refresh,
            httponly=True,
            samesite='lax',
            secure=False,
        )
        response.set_cookie(
            key='csrftoken',
            value=csrf,
            httponly=False,
            samesite='lax',
            secure=False,
        )
    def create_refresh_session(self, refresh_token: str, user: User):
        self.orm.create_refresh_session(refresh_token, user)
    
# transferir para self.tokrn_service




def get_payload(token_full):
    if not token_full:
        raise HttpError(401,'Token não fornecido')
    if token_full.startswith('Bearer '):
        token = token_full.split(' ')[1]
    else:
        token = token_full
    try:
        payload = jwt.decode(token, CHAVE, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HttpError(401, "Token expirado")
    except jwt.InvalidTokenError:
        raise HttpError(401,"Token inválido")