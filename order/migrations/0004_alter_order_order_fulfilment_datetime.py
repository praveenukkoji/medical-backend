# Generated by Django 3.2.3 on 2021-05-30 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_order_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_fulfilment_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]
