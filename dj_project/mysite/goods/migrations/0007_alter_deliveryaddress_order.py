# Generated by Django 4.0.6 on 2022-09-20 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_alter_deliveryaddress_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryaddress',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='goods.book'),
        ),
    ]