# Generated by Django 3.2 on 2021-04-27 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courierParcelApp', '0007_alter_order_charge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='merchant_nm',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='courierParcelApp.merchants'),
        ),
    ]
