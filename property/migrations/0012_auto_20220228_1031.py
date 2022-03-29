# Generated by Django 2.2.24 on 2022-02-28 07:31

from django.db import migrations
import phonenumbers
import phonenumber_field.modelfields


def validate_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(number):
            flat.owner_pure_phone = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца'),
        ),
        migrations.RunPython(validate_numbers)
    ]
