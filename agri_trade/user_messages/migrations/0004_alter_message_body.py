# Generated by Django 4.1.2 on 2022-11-07 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_messages', '0003_message_is_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(max_length=1500),
        ),
    ]
