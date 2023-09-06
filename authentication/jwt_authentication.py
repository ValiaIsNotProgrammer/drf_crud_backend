from contextvars import Token
from typing import Optional, Tuple
from rest_framework.request import Request
from rest_framework_simplejwt.authentication import AuthUser, JWTAuthentication


class CustomJWTAuthentication(JWTAuthentication):

    def authenticate(self, request: Request) -> Optional[Tuple[AuthUser, Token]]:

        # --------- overridden method because JWT has "Bearer " and needs to be retrieved   ------------

        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        if raw_token.startswith(b'Bearer '):
            raw_token = raw_token.split(' ')[1]


        validated_token = self.get_validated_token(raw_token)

        return self.get_user(validated_token), validated_token
