# Generated by Django 4.2.2 on 2023-06-07 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car',
            field=models.CharField(choices=[('Sports Car', 'Sports Car'), ('Pickup', 'Pickup'), ('Crossover', 'Crossover'), ('Minibus', 'Minibus'), ('Other', 'Other')], max_length=10, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_image',
            field=models.URLField(verbose_name='Image URL'),
        ),
    ]
