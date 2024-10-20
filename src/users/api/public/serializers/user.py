from rest_framework.serializers import ModelSerializer

from users.models import User


__all__ = [
    'UserReadSerializer',
    'UserCreateSerializer',
    'UserUpdateSerializer',
]


class UserReadSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'mobile',
            'created_at',
            'updated_at',
            'is_staff',
            'is_superuser',
            'is_active',
        ]


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['mobile', 'password']

    def create(self, validated_data):
        mobile = validated_data.get('mobile')
        password = validated_data.get('password')
        user = User.objects.create_user(mobile, password)
        return user

    def update(self, instance, validated_data):
        raise Exception('should not be used')

    def to_representation(self, instance):
        return UserReadSerializer(instance).data


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['password']

    def create(self, validated_data):
        raise Exception('should not be used')

    def update(self, instance, validated_data):
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
            instance.save()
        return instance

    def to_representation(self, instance):
        return UserReadSerializer(instance).data
