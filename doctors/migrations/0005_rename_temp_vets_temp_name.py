# Generated by Django 4.2.2 on 2023-06-24 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0004_vets_temp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vets',
            old_name='temp',
            new_name='temp_name',
        ),
    ]
