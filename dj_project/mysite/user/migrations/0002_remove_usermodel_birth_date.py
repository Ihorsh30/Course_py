# Generated by Django 4.0.6 on 2022-08-25 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='birth_date',
        ),
    ]
