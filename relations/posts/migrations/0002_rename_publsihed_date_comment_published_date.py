# Generated by Django 5.1.2 on 2024-10-30 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='publsihed_date',
            new_name='published_date',
        ),
    ]
