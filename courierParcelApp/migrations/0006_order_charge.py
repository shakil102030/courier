# Generated by Django 3.2 on 2021-04-27 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courierParcelApp', '0005_auto_20210427_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='charge',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
