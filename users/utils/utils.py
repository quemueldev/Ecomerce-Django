from ..schemas import EmailSchema
import random
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from ninja.errors import HttpError
from ..models import VerificationCode
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import jwt
from django.contrib.auth.models import User
from ..services.erros import *
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import authenticate

EMAIL = settings.EMAIL_HOST_USER
CHAVE = settings.SECRET_KEY

class EmailUtils:
    def __init__(self, email: str):
        self.email = email
    def validate_user(self, password: str) -> User:
        user = authenticate(username= self.email, password= password)
    
        if user is None:
            #ta caido aqui
            
            raise UserIsNoneError()
        return user

    def generate_code(self) -> str:
        return str(random.randint(100000, 999999))
       
    def validate_email(self) -> None:
        self.validate_format_email()


    def generate_payload(self) -> dict:
        payload = {
            'email': self.email,
            'verify': True,
            'exp': int((timezone.now() + timedelta(minutes=15)).timestamp())
        }
        return payload
    def validate_payload(self, payload) -> None:
        if payload['verify'] is not True:
            raise NotPermitedToRegister()
        
        if payload.get('email') != self.email:
            raise EmailDiferentForToken()
    
    def validate_len_data(self,data) -> None:
        if len(data.dict()['password']) < 6:
            raise MinValuePasswordError()
        
        if len(data.dict()['name']) < 3:
            raise MinValueNameError()
        
    # auxiliares
    def validate_format_email(self) -> None:
        try:
            validate_email(self.email)
            return True
        except ValidationError:
            raise InvalidEmailError()
    def serialize_user(self, user: User) -> dict:
        return {
            'id': user.id,
            'email': user.username,
            'nome': user.first_name,
            'e_admin': user.is_superuser
        }
    