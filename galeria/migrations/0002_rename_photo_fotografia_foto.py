# Generated by Django 5.0.1 on 2024-01-30 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotografia',
            old_name='photo',
            new_name='foto',
        ),
    ]
