from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver

from agri_trade.marketplace.models import Product

UserModel = get_user_model()


class Company(models.Model):
    COMPANY_NAME_MAX_LENGTH = 100
    COMPANY_VAT_MAX_LENGTH = 25
    COMPANY_ADDRESS_MAX_LENGTH = 200
    COMPANY_POSTCODE_MAX_LENGTH = 15
    COMPANY_LOCATION_MAX_LENGTH = 25
    COMPANY_COUNTRY_MAX_LENGTH = 25
    COMPANY_DESCRIPTION_MAX_LENGTH = 500

    account = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=CASCADE,
    )

    name = models.CharField(
        max_length=COMPANY_NAME_MAX_LENGTH,
        blank=True,
    )

    vat = models.CharField(
        max_length=COMPANY_VAT_MAX_LENGTH,
        blank=True,
    )

    address = models.TextField(
        max_length=COMPANY_ADDRESS_MAX_LENGTH,
        blank=True,
    )

    postcode = models.CharField(
        max_length=COMPANY_POSTCODE_MAX_LENGTH,
        blank=True,
    )

    location = models.CharField(
        max_length=COMPANY_LOCATION_MAX_LENGTH,
        blank=True,
    )

    country = models.CharField(
        max_length=COMPANY_COUNTRY_MAX_LENGTH,
        blank=True,
    )

    description = models.TextField(
        max_length=COMPANY_DESCRIPTION_MAX_LENGTH,
        blank=True,
    )

    favourites = models.ManyToManyField(
        Product,
        blank=True,
    )

    updated_on = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name


@receiver(post_save, sender=UserModel)
def create_company(sender, instance, created, **kwargs):
    if created:
        Company.objects.create(account_id=instance.id)


@receiver(post_save, sender=UserModel)
def save_company(sender, instance, **kwargs):
    instance.company.save()
