# Generated by Django 4.0.6 on 2022-08-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0009_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
