# Generated by Django 4.0.2 on 2023-02-15 13:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 15, 13, 23, 27, 811658, tzinfo=utc)),
        ),
    ]