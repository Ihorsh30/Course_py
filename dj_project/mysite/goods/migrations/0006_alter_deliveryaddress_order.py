# Generated by Django 4.0.6 on 2022-09-20 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_remove_book_address_remove_book_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryaddress',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.product'),
        ),
    ]