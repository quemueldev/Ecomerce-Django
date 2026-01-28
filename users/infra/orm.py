from django.conf import settings
from ..models import VerificationCode
from django.contrib.auth.models import User
from django.db import IntegrityError
from ..services.erros import *

EMAIL = settings.EMAIL_HOST_USER
CHAVE = settings.SECRET_KEY

class EmailOrm:
    def __init__(self, email):
        self.email = email
        
    def create_user(self, data) -> User:
        try:
            user = User.objects.create_user(
                username=self.email,
                first_name = data.name,
                password = data.password
            )
            return user
        except IntegrityError:
            raise EmailAlreadyInUseError()
        
    def delete_old_codes(self):
        VerificationCode.objects.filter(email=self.email).delete()

    def insert_to_db(self, code) -> str:
        try:
            VerificationCode.objects.create(email = self.email, code = code)
            return code
        except Exception as e:
            raise InternalError()
    def code_to_db(self, code_gerated):
        self.delete_old_codes()
        code = self.insert_to_db(code_gerated)
        return code
    def validate_is_unique(self):
        if User.objects.filter(username= self.email).exists():
            raise EmailAlreadyInUseError()
    def verify(self,code):
        try:
            vc = VerificationCode.objects.get(email=self.email,code=code)
        except VerificationCode.DoesNotExist:
            raise CodeDoesntExist()
        
        if vc.is_expired():
            raise ExpiredCode()
    def create_refresh_session(self, refresh_token: str, user: User):
        from core.models import RefreshSession
        try:
            RefreshSession.objects.filter(user=user).delete()

            RefreshSession.objects.create(
                user=user,
                token=refresh_token
            )
        except IntegrityError:
            raise IntegrityError()
        except Exception as e:
            print(e)
            raise InternalError()