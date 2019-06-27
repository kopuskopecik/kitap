from django.db import models
from django.urls import reverse

STATUS_CHOICES = (
	('a', 10),
    ('b', 15),
    ('c', 20),
    ('d', 25),
	('e', 30),
	('f', 35),
	('g', 40),
	('h', 45),
)

SAYFA_SAYISI = (
	('a', 1500),
    ('b', 2500),
)


class Category(models.Model):
    name = models.CharField("kategori adı", max_length=150, db_index=True)
    slug = models.SlugField("internet adresi",max_length=150, unique=True ,db_index=True)
    image1 = models.ImageField("Madalyalı Resim ", blank=True, null = True)
    image2 = models.ImageField("Madalyalı Resim", blank=True, null = True)
    sayi = models.PositiveIntegerField("Sıralama Sayısı")
    aktif = models.BooleanField("Aktif mi?", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('sayi', )
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Resim(models.Model):
	isim = models.CharField("resim adı", max_length=100)
	image = models.ImageField("resim", blank=True, null = True)

	def __str__(self):
		return self.isim

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name = "kategori")
    name = models.CharField("ürün adı", max_length=100, db_index=True)
    slug = models.SlugField("internet adresi",max_length=100, db_index=True)
    description = models.TextField("Ürün açıklaması", blank=True)
    price = models.DecimalField("fiyat", max_digits=10, decimal_places=2)
    available = models.BooleanField("mevcut mu?", default=True)
    sayfa_sayısı = models.CharField('sayfa sayısı', max_length=1, choices=SAYFA_SAYISI)
    ogrenci_sayisi = models.CharField(max_length=1, choices=STATUS_CHOICES)
    stock = models.PositiveIntegerField("stok miktarı",default = 100)
    agırlık = models.PositiveIntegerField("Ağırlık",default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField("Ürün resim", blank=True, null = True)
    odul = models.BooleanField("Madalyalı Madalyasız?", default=False)
    resimler = models.ManyToManyField(Resim, blank = True, verbose_name = "Nasıl Uygulanır Resimleri")
	
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
		

	
