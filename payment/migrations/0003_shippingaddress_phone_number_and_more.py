# Generated by Django 5.1.4 on 2024-12-10 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='phone_number',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='pickup_station',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='town',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.shippingaddress'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='address2',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
