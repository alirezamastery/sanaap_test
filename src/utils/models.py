from django.db import models


__all__ = [
    'TimestampModel',
]


class TimestampModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
