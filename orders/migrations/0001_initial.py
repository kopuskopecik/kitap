# Generated by Django 2.0 on 2019-07-16 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kargo_tipi', models.CharField(choices=[('1', 'Kapıda Nakit Ödeme'), ('2', 'Kapıda Tek Çekim Kredi Kartı Ödeme'), ('3', 'EFT ile Ödeme')], help_text='Blabla', max_length=10, verbose_name='Ödeme Tercihiniz:')),
                ('first_name', models.CharField(max_length=60, verbose_name='Adınız:')),
                ('last_name', models.CharField(max_length=60, verbose_name='Soyadınız:')),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(verbose_name='Adres:')),
                ('city', models.CharField(choices=[['1', 'Adana'], ['2', 'Adıyaman'], ['3', 'Afyonkarahisar'], ['4', 'Ağrı'], ['5', 'Aksaray'], ['6', 'Amasya'], ['7', 'Ankara'], ['8', 'Antalya'], ['9', 'Ardahan'], ['10', 'Artvin'], ['11', 'Aydın'], ['12', 'Balıkesir'], ['13', 'Bartın'], ['14', 'Batman'], ['15', 'Bayburt'], ['16', 'Bilecik'], ['17', 'Bingöl'], ['18', 'Bitlis'], ['19', 'Bolu'], ['20', 'Burdur'], ['21', 'Bursa'], ['22', 'Çanakkale'], ['23', 'Çankırı'], ['24', 'Çorum'], ['25', 'Denizli'], ['26', 'Diyarbakır'], ['27', 'Düzce'], ['28', 'Edirne'], ['29', 'Elazığ'], ['30', 'Erzincan'], ['31', 'Erzurum'], ['32', 'Eskişehir'], ['33', 'Gaziantep'], ['34', 'Giresun'], ['35', 'Gümüşhane'], ['36', 'Hakkâri'], ['37', 'Hatay'], ['38', 'Iğdır'], ['39', 'Isparta'], ['40', 'İstanbul'], ['41', 'İzmir'], ['42', 'Kahramanmaraş'], ['43', 'Karabük'], ['44', 'Karaman'], ['45', 'Kars'], ['46', 'Kastamonu'], ['47', 'Kayseri'], ['48', 'Kilis'], ['49', 'Kırıkkale'], ['50', 'Kırklareli'], ['51', 'Kırşehir'], ['52', 'Kocaeli'], ['53', 'Konya'], ['54', 'Kütahya'], ['55', 'Malatya'], ['56', 'Manisa'], ['57', 'Mardin'], ['58', 'Mersin'], ['59', 'Muğla'], ['60', 'Muş'], ['61', 'Nevşehir'], ['62', 'Niğde'], ['63', 'Ordu'], ['64', 'Osmaniye'], ['65', 'Rize'], ['66', 'Sakarya'], ['67', 'Samsun'], ['68', 'Şanlıurfa'], ['69', 'Siirt'], ['70', 'Sinop'], ['71', 'Sivas'], ['72', 'Şırnak'], ['73', 'Tekirdağ'], ['74', 'Tokat'], ['75', 'Trabzon'], ['76', 'Tunceli'], ['77', 'Uşak'], ['78', 'Van'], ['79', 'Yalova'], ['80', 'Yozgat'], ['81', 'Zonguldak']], max_length=10, verbose_name='Şehir:')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False, verbose_name='Ödenme durumu')),
            ],
            options={
                'verbose_name': 'Sipariş',
                'verbose_name_plural': 'Siparişler',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Fiyat')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Miktar')),
                ('agırlık', models.PositiveIntegerField(default=0, verbose_name='Ağırlık')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order', verbose_name='Sipariş')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='Ürün')),
            ],
        ),
    ]
