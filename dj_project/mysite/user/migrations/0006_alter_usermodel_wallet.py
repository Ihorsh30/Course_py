# Generated by Django 4.0.6 on 2022-09-16 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_usermodel_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='wallet',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
