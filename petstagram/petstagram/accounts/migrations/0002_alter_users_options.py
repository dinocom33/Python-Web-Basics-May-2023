# Generated by Django 4.2.1 on 2023-05-27 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ('username',)},
        ),
    ]