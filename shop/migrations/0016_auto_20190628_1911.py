# Generated by Django 2.0 on 2019-06-28 16:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20190628_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Ürün açıklaması'),
        ),
    ]
