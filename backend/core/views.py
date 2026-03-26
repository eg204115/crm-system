from rest_framework_simplejwt.views import TokenViewBase
from .serializers import CustomTokenSerializer

class CustomTokenView(TokenViewBase):
    serializer_class = CustomTokenSerializer