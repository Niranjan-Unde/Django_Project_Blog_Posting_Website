# Generated by Django 4.1.5 on 2023-02-13 10:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_rename_sdet_post_sdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateField(default=datetime.date(2023, 2, 13)),
        ),
    ]
