# Generated by Django 5.1.5 on 2025-02-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='rating_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='service',
            name='total_rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
