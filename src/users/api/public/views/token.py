from rest_framework_simplejwt.views import TokenObtainPairView

from users.api.public.serializers.token import CustomTokenObtainSerializer


__all__ = [
    'CustomTokenObtainPairView',
]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer
