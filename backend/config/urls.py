from django.contrib import admin
from django.urls import path
from core.serializers import CustomTokenSerializer

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenViewBase
)
from rest_framework.routers import DefaultRouter
from core.views import CompanyViewSet, ContactViewSet


class CustomTokenView(TokenViewBase):
    serializer_class = CustomTokenSerializer

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT endpoints
    path('api/v1/token/', CustomTokenView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', CustomTokenView.as_view(), name='token_refresh'),
]


# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     path('api/v1/', include(router.urls)),
# ]
router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'contacts', ContactViewSet, basename='contact')