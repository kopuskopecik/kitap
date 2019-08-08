# Generated by Django 2.0 on 2019-08-06 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0004_auto_20190806_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='genel',
            name='aktif',
            field=models.BooleanField(default=False, verbose_name='aktif mi'),
        ),
        migrations.AddField(
            model_name='genel',
            name='sira',
            field=models.PositiveIntegerField(default=0, verbose_name='Sıralama Sayısı'),
        ),
    ]