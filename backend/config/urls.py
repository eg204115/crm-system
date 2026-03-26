from django.contrib import admin
from django.urls import path
from core.serializers import CustomTokenSerializer

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenViewBase
)


class CustomTokenView(TokenViewBase):
    serializer_class = CustomTokenSerializer

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT endpoints
    path('api/v1/token/', CustomTokenView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', CustomTokenView.as_view(), name='token_refresh'),
]