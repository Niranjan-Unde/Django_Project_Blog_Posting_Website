# Generated by Django 4.1.5 on 2023-03-03 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_alter_post_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='uid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
