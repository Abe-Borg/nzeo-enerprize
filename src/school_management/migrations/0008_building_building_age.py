# Generated by Django 5.0 on 2024-01-28 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0007_rename_equipment_storage_btu_kwh_equipment_equipment_storage_kbtu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='building_age',
            field=models.IntegerField(default=0),
        ),
    ]
