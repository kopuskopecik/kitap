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
	slug = models.SlugField("internet adresi",max_length=150, unique=True ,db_index=True, help_text = "Burası yalnızca site-dizaynı için. Dokunmayınız!")
	sayfa_durumu = models.BooleanField("Sayfa Sayısı Var mı?", help_text = "1500-2500 gibi sayfa sayısı varsa işaretlenecek", default = False,)
	bireysel_mi = models.BooleanField("Bireysel mi", help_text = "Öğrencilerle beraber oynanMAyacaksa işaretlenecek!!!", default = False,)
	sadece_madalyalı_mı = models.BooleanField("Sadece Madalya mı", default = False, help_text = "Herhangi bir oyun olmaksızın bir kategori ise işaretlenecek Örneğin; sadece madalya için")
	sıralama_sayısı = models.PositiveIntegerField("Sıralama Sayısı")
	aktif = models.BooleanField("Aktif mi?", help_text="Sitede görünmesini istiyorsanız işaretleyiniz!!!", default = False,)
	
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
		
	class Meta:
		ordering = ('isim', )
		verbose_name = 'Resim'
		verbose_name_plural = 'Resimler'
		
class Resim(models.Model):
	isim = models.CharField("resim adı", max_length=100)
	resimler = models.ManyToManyField(TekliResim, verbose_name = "resimler", blank=True)

	class Meta:
		ordering = ('isim', )
		verbose_name = 'Resim-Grubu'
		verbose_name_plural = 'Resim-Grupları'

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
    madalyalı_mı = models.BooleanField("Madalyalı mı", default = True)
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
    anasayfada_gosterilsin_mi = models.BooleanField("AnaSayfada gösterilsin mi?", default = False, help_text = "Anasayfada gösterilmesi istenen ürünler için işaretlenecektir.")
	
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
		

	
