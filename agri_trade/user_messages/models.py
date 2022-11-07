from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE

UserModel = get_user_model()


class Message(models.Model):
    sender = models.ForeignKey(
        UserModel,
        on_delete=CASCADE,
        related_name='sender',
    )

    receiver = models.ForeignKey(
        UserModel,
        on_delete=CASCADE,
        related_name='receiver',
    )

    body = models.TextField(
        max_length=500,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    is_read = models.BooleanField(
        default=False,
    )

