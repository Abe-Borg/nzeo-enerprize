# Generated by Django 5.0 on 2024-02-10 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0010_rename_meter_fwd_kwh_meter_meter_fwd_kwh_usage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='school_student_percent_disenfrachised',
            new_name='school_student_percent_disadvantaged',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='school_student_percent_low_income',
            new_name='school_student_percent_english_learners',
        ),
    ]
