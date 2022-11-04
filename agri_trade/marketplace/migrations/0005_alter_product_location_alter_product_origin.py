# Generated by Django 4.1.2 on 2022-11-04 10:52

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_alter_product_location_alter_product_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='location',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='origin',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
    ]
