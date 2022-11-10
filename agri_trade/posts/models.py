from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE

UserModel = get_user_model()


class Post(models.Model):
    TOPIC_MAX_LEN = 50

    SUBTOPIC_MAX_LEN = 50

    author = models.ForeignKey(
        UserModel,
        on_delete=CASCADE,
        related_name='blog_posts',
    )

    topic = models.CharField(
        max_length=TOPIC_MAX_LEN,
    )

    subtopic = models.CharField(
        max_length=SUBTOPIC_MAX_LEN,
        blank=True,
        null=True,
    )

    body = models.TextField()

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.topic} - {self.author}'


