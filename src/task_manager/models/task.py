import uuid

from django.db import models
from django.contrib.auth import get_user_model

from utils.models import TimestampModel


__all__ = [
    'Task',
]

User = get_user_model()


class Task(TimestampModel):
    class Status(models.TextChoices):
        PENDING = 'PENDING'
        RUNNING = 'RUNNING'
        FAILED = 'FAILED'
        COMPLETED = 'COMPLETED'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    status = models.CharField(choices=Status.choices, default=Status.PENDING)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title
