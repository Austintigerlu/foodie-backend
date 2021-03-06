# Generated by Django 4.0.5 on 2022-06-07 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_location_restaurant_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='coordinates',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='hours',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]
