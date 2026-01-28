from ninja.security import APIKeyCookie
from django.contrib.auth import get_user_model
from ..models import RefreshSession

User = get_user_model()

class CookieJWTAuth(APIKeyCookie):
    param_name = "refresh"   # o key pega esse nome do cookie

    def authenticate(self, request, key): #o cookie ja vem em key
        print('aqui')
        refresh = key
        if not refresh:
            print('nenhum refresh')
            return None

        try:
            session = RefreshSession.objects.get(token=refresh, revoked=False)

            user = session.user
            if not user.is_superuser:
                print('não é admin')
                return None

            return (user, session)

        except RefreshSession.DoesNotExist:
            print('sessão não existe')
            return None
        except User.DoesNotExist:
            print('usuário não existe')
            return None
