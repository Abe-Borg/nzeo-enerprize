# Generated by Django 5.0 on 2024-02-29 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0045_performancemetrics_elec_energy_use_intensity_kwh_per_sqft_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='school_type',
            field=models.CharField(choices=[('pre_school', 'Pre-School'), ('middle_school', 'Middle School'), ('special_education_school', 'Special Education School'), ('elementary_school', 'Elementary School'), ('high_school', 'High School'), ('adult_school', 'Adult School'), ('miscellaneous', 'Miscellaneous')], max_length=100),
        ),
    ]
