# Generated by Django 2.0 on 2019-06-22 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190622_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ogrenci_sayisi',
            field=models.CharField(choices=[('a', 15), ('b', 20), ('c', 25), ('d', 30), ('e', 35), ('f', 40), ('g', 45)], max_length=1),
        ),
    ]
