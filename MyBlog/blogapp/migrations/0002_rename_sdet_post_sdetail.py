# Generated by Django 4.1.5 on 2023-02-11 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='sdet',
            new_name='sdetail',
        ),
    ]
