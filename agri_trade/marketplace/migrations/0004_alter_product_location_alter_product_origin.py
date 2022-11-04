# Generated by Django 4.1.2 on 2022-11-04 10:44

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_alter_product_created_on_alter_product_edited_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='location',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='origin',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]