# Generated by Django 2.2.24 on 2022-03-01 20:48

from django.db import migrations


def link_owner_flat(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    all_flats = Flat.objects.all()
    for flat in all_flats:
        owner = Owner.objects.filter(name=flat.owner_name).first()
        owner.my_flats.set(all_flats.filter(owner_name=flat.owner_name))


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20220301_2214'),
    ]

    operations = [
        migrations.RunPython(link_owner_flat)
    ]
