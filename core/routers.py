from ninja import Router
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from django.middleware.csrf import get_token
router_core = Router()

@router_core.post('refresh/')
def refresh(request):
    token = request.COOKIES.get("refresh_token")
    if not token:
        pass
    response = JsonResponse({'retorno': 'token renovado'})
    try:
        refresh = RefreshToken(token)
        new_access = refresh.access_token

        
        response.set_cookie(
            key='access_token',
            value=str(new_access),
            httponly=True,
            samesite='Lax'
        )
        return response
    except Exception:
        return response.delete_cookie('refresh_token')
    response = JsonResponse({'retorno': 'token renovado'})
    return response