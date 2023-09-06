from rest_framework_simplejwt.tokens import RefreshToken


def generate_jwt_data(user):
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)
    return access_token, refresh_token


def save_jwt_data(access_token, refresh_token, user):
    user.access_token = "Bearer " + access_token
    user.refresh_token = "Bearer " + refresh_token
    user.save()