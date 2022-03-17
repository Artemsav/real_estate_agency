# Generated by Django 2.2.24 on 2022-03-17 11:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_auto_20220317_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes_owner', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
