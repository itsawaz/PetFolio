# Generated by Django 4.2.2 on 2023-06-24 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 24, 8, 22, 20, 467834, tzinfo=datetime.timezone.utc)),
        ),
    ]
