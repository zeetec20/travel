# Generated by Django 3.0.2 on 2020-01-15 16:59

from django.db import migrations
import image_cropping.fields
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200115_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimoni',
            name='fullname',
        ),
        migrations.AlterField(
            model_name='testimoni',
            name='cover',
            field=image_cropping.fields.ImageCropField(upload_to=users.models.Testimoni.path_upload),
        ),
    ]
