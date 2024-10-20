from rest_framework import serializers

from task_manager.models import Task
from users.models import User


__all__ = [
    'TaskReadSerializer',
    'TaskWriteSerializer',
]


class _UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'mobile',
        ]


class TaskReadSerializer(serializers.ModelSerializer):
    user = _UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


class TaskWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'title',
            'status',
        ]

    def validate(self, attrs):
        request = self.context.get('request')
        assert request is not None, 'request object is needed'

        attrs['user'] = request.user

        return attrs

    def update(self, instance, validated_data):
        validated_data.pop('user')
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        return TaskReadSerializer(instance).data
