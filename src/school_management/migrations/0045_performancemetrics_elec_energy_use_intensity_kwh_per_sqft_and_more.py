# Generated by Django 5.0 on 2024-02-28 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0044_alter_school_school_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='performancemetrics',
            name='elec_energy_use_intensity_kwh_per_sqft',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='school',
            name='school_type',
            field=models.CharField(choices=[('middle_school', 'Middle School'), ('special_education_school', 'Special Education School'), ('pre_school', 'Pre-School'), ('high_school', 'High School'), ('elementary_school', 'Elementary School'), ('miscellaneous', 'Miscellaneous'), ('adult_school', 'Adult School')], max_length=100),
        ),
    ]
