# Generated by Django 2.0 on 2019-08-07 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0005_auto_20190806_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='slayt',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Kare Resim'),
        ),
        migrations.AlterField(
            model_name='slayt',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Dikdörtgen Resim'),
        ),
    ]
