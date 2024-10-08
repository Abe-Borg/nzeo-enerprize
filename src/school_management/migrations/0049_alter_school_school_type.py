# Generated by Django 5.0 on 2024-03-08 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0048_alter_meterreading_demand_charge_kw_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='school_type',
            field=models.CharField(choices=[('middle_school', 'Middle School'), ('miscellaneous', 'Miscellaneous'), ('elementary_school', 'Elementary School'), ('high_school', 'High School'), ('pre_school', 'Pre-School'), ('special_education_school', 'Special Education School'), ('adult_school', 'Adult School')], max_length=100),
        ),
    ]
