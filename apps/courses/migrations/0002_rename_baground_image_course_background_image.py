# Generated by Django 3.2.9 on 2021-11-03 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='baground_image',
            new_name='background_image',
        ),
    ]
