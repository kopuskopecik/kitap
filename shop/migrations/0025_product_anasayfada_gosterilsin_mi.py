# Generated by Django 2.0 on 2019-07-02 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_remove_product_anasayfada_gosterilsin_mi'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='anasayfada_gosterilsin_mi',
            field=models.BooleanField(default=False, help_text='Anasayfada gösterilmesi istenen ürünler için işaretlenecektir.', verbose_name='AnaSayfada gösterilsin mi?'),
        ),
    ]
