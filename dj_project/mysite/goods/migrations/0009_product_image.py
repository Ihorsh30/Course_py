# Generated by Django 4.0.6 on 2022-08-15 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]