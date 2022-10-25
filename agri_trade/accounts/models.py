from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver

UserModel = get_user_model()


class Company(models.Model):
    account = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=CASCADE,
    )

    name = models.CharField(
        max_length=100,
        blank=True,
    )

    vat = models.CharField(
        max_length=25,
        blank=True,
    )

    address = models.TextField(
        max_length=200,
        blank=True,
    )

    postcode = models.CharField(
        max_length=15,
        blank=True,
    )

    location = models.CharField(
        max_length=25,
        blank=True,
    )

    country = models.CharField(
        max_length=25,
        blank=True,
    )

    description = models.TextField(
        max_length=500,
        blank=True,
    )

    updated_on = models.DateTimeField(
        auto_now_add=True,
    )


@receiver(post_save, sender=UserModel)
def create_company(sender, instance, created, **kwargs):
    if created:
        Company.objects.create(account_id=instance.id)


@receiver(post_save, sender=UserModel)
def save_company(sender, instance, **kwargs):
    instance.company.save()
