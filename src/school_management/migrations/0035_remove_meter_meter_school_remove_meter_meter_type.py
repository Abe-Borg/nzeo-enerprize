# Generated by Django 5.0 on 2024-02-19 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0034_alter_meter_meter_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meter',
            name='meter_school',
        ),
        migrations.RemoveField(
            model_name='meter',
            name='meter_type',
        ),
    ]
