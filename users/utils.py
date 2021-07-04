import jwt
import json

from django.http    import JsonResponse

from my_settings    import SECRET_KEY
from users.models   import User

class ConfirmUser:
    def __init__(self, func):
        self.func = func

    def __call__(self, request, *arg, **kargs):
        try:
            access_token = request.headers.get('Authorization', None)
            if access_token:
                payload = jwt.decode( access_token, SECRET_KEY, algorithms='HS256' )
                login_user = User.objects.get(id=payload["user"])
                request.user = login_user
                return self.func(self, request, *arg, **kargs)

            return JsonResponse({"MESSAGE" : "NEED LOGIN"}, status=401)

        except jwt.exceptions.DecodeError:
            return JsonResponse({"MESSAGE" : "INVALID TOKEN"}, status=401)

        except User.DoesNotExist:
            return JsonResponse({"MESSAGE" : "INVALID USER"}, status=401)