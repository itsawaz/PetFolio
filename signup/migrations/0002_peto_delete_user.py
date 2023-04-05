# Generated by Django 4.1.7 on 2023-04-05 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('pet_type', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
