# Generated by Django 2.0 on 2020-02-10 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genel',
            options={'ordering': ['-sira'], 'verbose_name': 'Genel-Konu', 'verbose_name_plural': 'Genel-Konular'},
        ),
    ]