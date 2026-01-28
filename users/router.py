from django.conf import settings
from django.http import JsonResponse
from django.middleware.csrf import get_token

import jwt 

from ninja_jwt.tokens import RefreshToken
from ninja import Router

from .schemas import SignInSchema,SignUpSchema,SendSchema,VerifySchema
from .services.erros import *
from .providers.container import build_email_service
from .services.http import domain_errors
from core.infra.security import CookieJWTAuth

auth = Router()
CHAVE = settings.SECRET_KEY

@auth.post(
    'codigo/', 
    tags=['auth']
    )
@domain_errors
def send_code(request, data: SendSchema):
    service = build_email_service(data.email)
    service.send_code()
    return {'retorno': 'sucesso'}


@auth.post(
    'verifica_codigo/', 
    tags=['auth']
    )
@domain_errors
def verify(request, data: VerifySchema):
    service = build_email_service(data.email)

    payload = service.verify_code(data.code)
    token = jwt.encode(payload, CHAVE, algorithm='HS256')
    return {'retorno': 'sucesso', 'token': token}


@auth.post(
    'cadastro/',
    tags=['auth']
    )
@domain_errors
def register(request, data: SignUpSchema):
    service = build_email_service(data.email)
    token = request.headers.get('Authorization')
    user = service.register(data, token)

    refresh = RefreshToken.for_user(user)
    access = refresh.access_token

    response = JsonResponse({'retorno': 'sucesso'})
    csrf = get_token(request)
    service.set_cookies(
        response, str(access), str(refresh), csrf
    )
    
    return response

   
@auth.post(
    'login/',
    tags=['auth']
    )
@domain_errors
def authenticate(request, data:SignInSchema):
    service = build_email_service(data.email)
    user = service.authenticate_user(data.password)
    refresh = RefreshToken.for_user(user)
    access = refresh.access_token
    user_fields = service.serialize_user(user)

    response = JsonResponse(
        {'retorno': 'sucesso', 'user': user_fields}
    )
    
    service.set_cookies(
        response, str(access), str(refresh), get_token(request)
    )
    
    service.create_refresh_session(str(refresh), user) #aqui 
   
    return response



@auth.get('meu_usuario', auth=CookieJWTAuth, tags=['auth'])
def get_my_user(request):
    user = request.user
    return {
        'id': user.id,
        'email': user.username,
        'nome': user.first_name,
        'e_admin': user.is_superuser
    }