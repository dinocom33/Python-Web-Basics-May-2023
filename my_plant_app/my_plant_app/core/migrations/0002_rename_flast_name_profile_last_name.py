# Generated by Django 4.2.2 on 2023-06-12 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='flast_name',
            new_name='last_name',
        ),
    ]
