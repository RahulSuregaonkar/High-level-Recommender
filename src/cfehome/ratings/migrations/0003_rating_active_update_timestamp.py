# Generated by Django 4.2.9 on 2024-01-29 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_alter_rating_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='active_update_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
