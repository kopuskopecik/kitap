# Generated by Django 2.0 on 2019-07-06 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0003_renkfont'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renkfont',
            name='kategorilerim_yazı_boyutu',
            field=models.CharField(blank=True, choices=[(8, '8'), (10, '10'), (12, '12'), (14, '14'), (16, '16'), (18, '18'), (20, '20'), (22, '22'), (24, '24')], max_length=30, verbose_name='KATEGORİLERİM başlığının yazı büyüklğü'),
        ),
        migrations.AlterField(
            model_name='renkfont',
            name='urunler_yazı_boyutu',
            field=models.CharField(blank=True, choices=[(8, '8'), (10, '10'), (12, '12'), (14, '14'), (16, '16'), (18, '18'), (20, '20'), (22, '22'), (24, '24')], max_length=30, verbose_name='Ürünler başlığının yazı büyüklğü'),
        ),
    ]
