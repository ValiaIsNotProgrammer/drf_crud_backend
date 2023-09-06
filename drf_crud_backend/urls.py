from django.contrib import admin
from django.shortcuts import redirect
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include, re_path
from authorization.views import CreateAuthorizationView
from authentication.views import AuthenticationView
from otp.views import OTPView
from profile.views import ProfileView
from drf_crud_backend.settings._settings.swagger import API_VERSION
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(fr'{AuthenticationView.name}', AuthenticationView)
router.register(fr'{OTPView.name}', OTPView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'api/{API_VERSION}/', include(router.urls)),
    path(f'api/{API_VERSION}/{ProfileView.name}/<str:email>/', ProfileView.as_view(), name='profile'),
    path(f'api/{API_VERSION}/{CreateAuthorizationView.name}', CreateAuthorizationView.as_view()),
    path(f'api/{API_VERSION}/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'api/{API_VERSION}/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("", lambda request: redirect("schema-swagger-ui"), name="redirect-to-swagger"),
]

