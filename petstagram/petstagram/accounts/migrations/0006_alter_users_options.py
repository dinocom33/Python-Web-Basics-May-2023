# Generated by Django 4.2.1 on 2023-06-02 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_users_first_name_users_last_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ('username',), 'verbose_name_plural': 'Users'},
        ),
    ]