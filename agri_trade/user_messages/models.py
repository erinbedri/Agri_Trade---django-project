from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE

UserModel = get_user_model()


class Message(models.Model):
    SUBJECT_MAX_LEN = 50

    BODY_MAX_LEN = 1500

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

    subject = models.CharField(
        max_length=SUBJECT_MAX_LEN,
    )

    body = models.TextField(
        max_length=BODY_MAX_LEN,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    is_read = models.BooleanField(
        default=False,
    )

