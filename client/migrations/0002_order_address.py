# Generated by Django 5.1.5 on 2025-02-28 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
