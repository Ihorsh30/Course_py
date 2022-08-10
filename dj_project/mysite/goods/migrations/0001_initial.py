# Generated by Django 4.0.6 on 2022-08-08 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=32)),
                ('product_type', models.SlugField(max_length=32)),
                ('product_cost', models.PositiveIntegerField(default=0)),
                ('product_quantity_stock', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=32)),
                ('product_type', models.SlugField(max_length=32)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
