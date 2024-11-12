from django.contrib.auth.models import AbstractUser

from django.db.models import (
    DateTimeField,
    CharField
)

class User(AbstractUser):
    created_at = DateTimeField(null=False, auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]