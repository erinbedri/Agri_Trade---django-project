# Generated by Django 4.1.2 on 2022-11-16 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_postcommentlike_postcommentdislike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcommentlike',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='postcommentlike',
            name='users',
        ),
        migrations.DeleteModel(
            name='PostCommentDislike',
        ),
        migrations.DeleteModel(
            name='PostCommentLike',
        ),
    ]