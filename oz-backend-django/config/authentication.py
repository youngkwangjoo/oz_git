from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import User
import jwt

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("jwt-auth")

        if not token:
            return None

        try:
            decoded = jwt.decode(token, 
			                     settings.SECRET_KEY, 
								 algorithms=["HS256"])
            user_id = decoded.get("id")

            if not user_id:
                raise AuthenticationFailed("Invalid Token")

            user = User.objects.get(id=user_id)
            return (user, None)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.DecodeError:
            raise AuthenticationFailed("Error decoding token")
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found")