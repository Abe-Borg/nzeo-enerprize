# Generated by Django 5.0 on 2024-01-27 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_rename_author_mapannotation_annotation_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapannotation',
            name='annotation_description',
            field=models.TextField(blank=True, default='annotation_description', max_length=100, null=True),
        ),
    ]
