# Generated by Django 3.2 on 2021-04-27 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courierParcelApp', '0008_alter_order_merchant_nm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='merchant_nm',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
