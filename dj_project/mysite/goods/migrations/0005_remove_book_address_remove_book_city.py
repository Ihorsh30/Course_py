# Generated by Django 4.0.6 on 2022-09-17 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_deliveryaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='address',
        ),
        migrations.RemoveField(
            model_name='book',
            name='city',
        ),
    ]
