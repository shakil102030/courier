# Generated by Django 3.2 on 2021-04-27 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courierParcelApp', '0006_order_charge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='charge',
            field=models.FloatField(blank=True),
        ),
    ]
