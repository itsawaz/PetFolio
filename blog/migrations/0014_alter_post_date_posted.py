# Generated by Django 4.2.2 on 2023-06-24 08:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 24, 8, 38, 43, 212887, tzinfo=datetime.timezone.utc)),
        ),
    ]
