# Generated by Django 4.2.1 on 2023-05-31 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_users_first_name_users_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='last_name',
        ),
    ]
