# Generated by Django 2.2.24 on 2022-03-01 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20220228_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
    ]
