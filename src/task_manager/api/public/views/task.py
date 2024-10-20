from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import SAFE_METHODS, BasePermission

from task_manager.models import Task
from task_manager.api.public.serializers.task import *
from task_manager.api.public.filters.task import *


__all__ = [
    'TaskViewSet'
]


class TaskPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and not (user.is_staff or user.is_superuser)  # API is for regular users only

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.order_by('created_at')
    filterset_class = TaskFilter
    permission_classes = [TaskPermission]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return TaskReadSerializer
        return TaskWriteSerializer
