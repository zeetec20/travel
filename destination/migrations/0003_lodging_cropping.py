# Generated by Django 3.0.2 on 2020-01-18 19:40

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0002_remove_lodging_cropping'),
    ]

    operations = [
        migrations.AddField(
            model_name='lodging',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '700x800', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
