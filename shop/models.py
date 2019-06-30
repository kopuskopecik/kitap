from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

STATUS_CHOICES = (
	('a', 0),
	('b', 10),
    ('c', 15),
    ('d', 20),
    ('e', 25),
	('f', 30),
	('g', 35),
	('h', 40),
	('i', 45),
)

SAYFA_SAYISI = (
	('a', 0),
	('a', 1000),
    ('b', 1500),
	('c', 2500),
)

class AnaCategory(models.Model):
	name = models.CharField("kategori adı", max_length=150, db_index=True)
	slug = models.SlugField("internet adresi",max_length=150, unique=True ,db_index=True)
	sayfa_durumu = models.BooleanField("Sayfa Sayısı Var mı?")
	bireysel_mi = models.BooleanField("Bireysel mi")
	sadece_madalyalı_mı = models.BooleanField("Etkinliksiz madalyalı mı")
	sıralama_sayısı = models.PositiveIntegerField("Sıralama Sayısı")
	aktif = models.BooleanField("Aktif mi?")
	
	class Meta:
		ordering = ('sıralama_sayısı', )
		verbose_name = 'Ana-Kategori'
		verbose_name_plural = 'Ana-Kategoriler'
	
	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('shop:product_list_by_category', args=[self.slug])

class TekliResim(models.Model):
	isim = models.CharField("resim adı", max_length=100)
	image1 = models.ImageField("resim")
	
	def __str__(self):
		return self.isim
		
class Resim(models.Model):
	isim = models.CharField("resim adı", max_length=100)
	resimler = models.ManyToManyField(TekliResim, verbose_name = "resimler", blank=True)

	def __str__(self):
		return self.isim

class Category(models.Model):
    ana_kategori = models.ForeignKey(AnaCategory, on_delete=models.CASCADE, verbose_name = "Ana Kategori")
    name = models.CharField("kategori adı", max_length=150, db_index=True)
    slug = models.SlugField("internet adresi",max_length=150, unique=True ,db_index=True)
    image1 = models.ImageField("Kategori Resmi", blank=True, null = True)
    nasıl_uygulanır_resimleri = models.ForeignKey(Resim, on_delete=models.CASCADE, blank = True, null = True,verbose_name = "Nasıl Uygulanır Resimleri", related_name= "nasil")
    odul_buttonu_resimleri = models.ForeignKey(Resim, on_delete=models.CASCADE, blank = True, null = True, verbose_name = "Kişiye özel Ödül Butonu Resimleri", related_name = 'odul')
    sayi = models.PositiveIntegerField("Sıralama Sayısı")
    madalyalı_mı = models.BooleanField("Madalyalı mı")
    sayfa_sayısı = models.CharField('sayfa sayısı', max_length=1, choices=SAYFA_SAYISI)
    

    class Meta:
        ordering = ('sayi', )
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name = "kategori")
    name = models.CharField("ürün adı", max_length=100, db_index=True)
    slug = models.SlugField("internet adresi",max_length=100, db_index=True)
    description = RichTextField("Ürün açıklaması", blank=True)
    price = models.DecimalField("fiyat", max_digits=10, decimal_places=2)
    agırlık = models.PositiveIntegerField("Ağırlık",default = 0)
    ogrenci_sayisi = models.CharField(max_length=1, choices=STATUS_CHOICES)
	
    class Meta:
        ordering = ('ogrenci_sayisi', )
        index_together = (('id', 'slug'),)
        verbose_name = 'Ürün'
        verbose_name_plural = "Ürünler"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
	
    def get_nasil_url(self):
        return reverse('shop:nasil', args=[self.id, self.slug])
		

	
