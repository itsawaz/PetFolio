# Generated by Django 4.1.7 on 2023-04-05 16:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_date_posted_alter_post_pet_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 5, 16, 19, 24, 476483, tzinfo=datetime.timezone.utc)),
        ),
    ]
