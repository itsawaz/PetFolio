# Generated by Django 4.2.2 on 2023-07-01 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
