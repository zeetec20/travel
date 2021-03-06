# Generated by Django 3.0.2 on 2020-01-20 01:13

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0005_auto_20200120_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '700x800', adapt_rotation=False, allow_fullsize=True, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
