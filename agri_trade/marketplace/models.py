from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CASCADE

from agri_trade.marketplace.validators import file_size

UserModel = get_user_model()


class Product(models.Model):
    PRODUCT_CATEGORY = [
        ('Cereals', 'Cereals'),
        ('Pulses', 'Pulses'),
        ('Nuts', 'Nuts'),
        ('Oilseeds', 'Oilseeds'),
        ('Sugar and starch', 'Sugar and starch'),
        ('Fiber Crops', 'Fiber Crops'),
        ('Beverages', 'Beverages'),
        ('Narcotics', 'Narcotics'),
        ('Spices', 'Spices'),
        ('Forages', 'Forages'),
        ('Vegetables', 'Vegetables'),
        ('Fruits', 'Fruits'),
    ]

    PRODUCT_TYPE_MAX_LEN = max([len(product_type[1]) for product_type in PRODUCT_CATEGORY])

    CULTIVATION_TYPES = [
        ('Organic', 'Organic'),
        ('Conventional', 'Conventional'),
        ('In Conversion', 'In Conversion'),
    ]

    CULTIVATION_TYPE_MAX_LEN = max([len(cultivation_type[1]) for cultivation_type in CULTIVATION_TYPES])

    owner = models.ForeignKey(
        UserModel,
        on_delete=CASCADE)

    name = models.CharField(
        max_length=20,
    )

    category = models.CharField(
        max_length=PRODUCT_TYPE_MAX_LEN,
        choices=PRODUCT_CATEGORY,
    )

    variety = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )

    type = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )

    form = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )

    size = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )

    cultivation_type = models.CharField(
        max_length=CULTIVATION_TYPE_MAX_LEN,
        choices=CULTIVATION_TYPES,
    )

    available_volume = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000000),
        ]
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(0),
        ]
    )

    description = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )

    origin = models.CharField(
        max_length=50,
    )

    location = models.CharField(
        max_length=50,
    )

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='produces',
        validators=(
            file_size,
        )
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    edited_on = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name
