# Generated by Django 4.2.9 on 2024-02-05 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_movie_rating_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
