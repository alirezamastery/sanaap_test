from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


__all__ = [
    'CustomTokenObtainSerializer',
]


class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    username_field = 'mobile'
