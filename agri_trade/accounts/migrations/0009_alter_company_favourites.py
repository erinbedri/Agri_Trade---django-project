# Generated by Django 4.1.2 on 2022-11-10 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0006_alter_product_location_alter_product_origin'),
        ('accounts', '0008_alter_company_favourites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='favourites',
            field=models.ManyToManyField(blank=True, to='marketplace.product'),
        ),
    ]
