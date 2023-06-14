# Generated by Django 4.2.2 on 2023-06-13 16:49

from django.db import migrations, models
import games_play_app.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_game_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='rating',
            field=models.FloatField(validators=[games_play_app.core.validators.rating_validator]),
        ),
    ]