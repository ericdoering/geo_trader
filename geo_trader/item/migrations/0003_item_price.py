# Generated by Django 3.2.23 on 2023-12-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20231211_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
