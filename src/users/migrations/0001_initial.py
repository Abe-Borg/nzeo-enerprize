# Generated by Django 5.0 on 2024-01-31 21:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('district_management', '0002_rename_district_bb_bottom_left_lat_schooldistrict_district_bb_northeast_lat_and_more'),
        ('school_management', '0008_building_building_age'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='district_management.schooldistrict')),
                ('user_school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_management.school')),
            ],
        ),
    ]
