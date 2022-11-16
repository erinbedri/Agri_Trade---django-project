from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE

UserModel = get_user_model()


class Post(models.Model):
    TITLE_MAX_LEN = 50

    SUBTITLE_MAX_LEN = 150

    TOPIC_CHOICES = (
        ('Agriculture', 'Agriculture'),
        ('Markets', 'Markets'),
        ('Technology', 'Technology'),
        ('Others', 'Others'),
    )

    TOPIC_MAX_LEN = max([len(topic[1]) for topic in TOPIC_CHOICES])

    author = models.ForeignKey(
        UserModel,
        on_delete=CASCADE,
        related_name='posts',
    )

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    subtitle = models.CharField(
        max_length=SUBTITLE_MAX_LEN,
        blank=True,
        null=True,
    )

    topic = models.CharField(
        max_length=TOPIC_MAX_LEN,
        choices=TOPIC_CHOICES,
    )

    body = RichTextField()

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


class PostComment(models.Model):
    COMMENT_MAX_LEN = 500

    author = models.ForeignKey(
        UserModel,
        on_delete=CASCADE,
    )

    post = models.ForeignKey(
        Post,
        on_delete=CASCADE,
    )

    body = models.TextField(
        max_length=COMMENT_MAX_LEN,
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'Comment by {self.author}.'







