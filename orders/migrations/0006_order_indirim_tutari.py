# Generated by Django 2.0 on 2019-08-07 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190806_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='indirim_tutari',
            field=models.PositiveIntegerField(default=0, verbose_name='İndirim Miktarı'),
        ),
    ]
