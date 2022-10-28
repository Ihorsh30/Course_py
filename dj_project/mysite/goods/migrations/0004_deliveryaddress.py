# Generated by Django 4.0.6 on 2022-09-17 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0003_bookitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default='', max_length=50)),
                ('city', models.CharField(max_length=32)),
                ('phone', models.CharField(blank=True, default='', max_length=50)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.book')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
