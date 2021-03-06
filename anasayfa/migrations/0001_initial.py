# Generated by Django 2.0 on 2019-08-16 13:28

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dokuman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50, verbose_name='Doküman Adı:')),
                ('slug', models.SlugField(max_length=130, unique=True)),
                ('dokuman_ekle', models.FileField(upload_to='', verbose_name='doküman yükle')),
                ('aktif', models.BooleanField(default=False, verbose_name='aktif mi')),
                ('sira', models.PositiveIntegerField(default=0, verbose_name='Sıralama Sayısı')),
            ],
            options={
                'verbose_name': 'Doküman',
                'verbose_name_plural': 'Dokümanlar',
            },
        ),
        migrations.CreateModel(
            name='Genel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('başlık', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=130, unique=True)),
                ('kısa_içerik', ckeditor.fields.RichTextField()),
                ('uzun_içerik', ckeditor.fields.RichTextField()),
                ('aktif', models.BooleanField(default=False, verbose_name='aktif mi')),
                ('sira', models.PositiveIntegerField(default=0, verbose_name='Sıralama Sayısı')),
                ('resim_grubu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resim_grubu', to='shop.Resim', verbose_name='Resim grubu')),
            ],
            options={
                'verbose_name': 'Genel-Konu',
                'verbose_name_plural': 'Genel-Konular',
            },
        ),
        migrations.CreateModel(
            name='Slayt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(blank=True, max_length=50, verbose_name='Başlık')),
                ('yazı', models.CharField(blank=True, max_length=200, verbose_name='Yazı')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Dikdörtgen Resim')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Kare Resim')),
                ('aktif', models.BooleanField(default=False, help_text='Sitede görünmesini istiyorsanız işaretleyiniz!!!', verbose_name='Aktif mi?')),
                ('sıralama_sayısı', models.PositiveIntegerField(default=0, verbose_name='Anasayfa Sıralama Sayısı')),
            ],
            options={
                'verbose_name': 'Slayt-Resmi',
                'verbose_name_plural': 'Slayt-Resimleri',
                'ordering': ['sıralama_sayısı'],
            },
        ),
        migrations.CreateModel(
            name='Yorum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50, verbose_name='Kullanıcı Adı:')),
                ('okul', models.CharField(choices=[('İlkokul', 'İlkokul'), ('Ortaokul', 'Ortaokul')], max_length=30, verbose_name='Okulunuz:')),
                ('content', models.TextField(verbose_name='Yorum:')),
                ('aktif', models.BooleanField(default=False, help_text='Sitede görünmesini istiyorsanız işaretleyiniz!!!', verbose_name='Aktif mi?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma tarihi')),
            ],
            options={
                'verbose_name': 'Yorum',
                'verbose_name_plural': 'Yorumlar',
                'ordering': ['-created_at'],
            },
        ),
    ]
