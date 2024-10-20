from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated, AllowAny

from users.models import User
from users.api.public.serializers.user import *


__all__ = [
    'UserViewSet',
]


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user == obj


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [UserPermission]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return UserReadSerializer
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserUpdateSerializer
