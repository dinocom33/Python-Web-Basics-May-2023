# Generated by Django 4.2.1 on 2023-05-27 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_alter_pet_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pet',
            options={'ordering': ('date_of_birth', 'name'), 'verbose_name_plural': 'Pets'},
        ),
        migrations.AlterField(
            model_name='pet',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
