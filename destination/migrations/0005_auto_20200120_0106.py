# Generated by Django 3.0.2 on 2020-01-20 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0004_destination_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]