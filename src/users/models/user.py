import re
import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError

from users.managers import UserManager
from utils.models import TimestampModel


__all__ = [
    'User'
]


def mobile_validator(value):
    if not re.match(r'^09\d{9}$', value):
        raise ValidationError('%(value)s is not a valid mobile number', params={'value': value})


class User(AbstractBaseUser, PermissionsMixin, TimestampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    mobile = models.CharField(max_length=15, unique=True, validators=[mobile_validator])

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'mobile'

    def __str__(self):
        return self.mobile
