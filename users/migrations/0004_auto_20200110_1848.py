# Generated by Django 3.0.2 on 2020-01-10 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200110_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='customer',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='fullname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='number_phone',
            field=models.IntegerField(null=True),
        ),
    ]