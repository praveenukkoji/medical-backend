# Generated by Django 3.2.3 on 2021-05-29 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storemedicine',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storemedicine',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
