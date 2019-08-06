from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from shop.models import Resim

FONT_RENKLERİ = (

("text-primary", "mavi"),
("text-secondary", "gri"),
("text-success", "yeşil"),
("text-danger", "kırmızı"),
("text-warning", "turuncu"),
("text-info", "açık mavi"),
("text-light", "ince beyaz"),
("text-dark", "koyu siyah"),
("text-body", "az koyu siyah"),
("text-muted", "sönük gri"),
("text-white", "kalın beyaz"),
("text-black-50", "ince siyah"),
("text-white-50", "kalın gri"),

)

OKULLAR = (

    ("İlkokul", "İlkokul"),
    ("Ortaokul", "Ortaokul"),
)

ARKA_PLAN_RENKLERİ = (

	("bg-primary", "mavi"),
	("bg-secondary", "gri"),
	("bg-success", "yeşil"),
	("bg-danger", "kırmızı"),
	("bg-warning", "turuncu"),
	("bg-info", "açık mavi"),
	("bg-light", "ince beyaz"),
	("bg-dark", "koyu siyah"),
	("bg-white", "kalın beyaz"),
	("bg-transparent", "ince siyah"),

)

BUTTON_RENKLERİ = (

	("btn-primary", "mavi"),
	("btn-secondary", "gri"),
	("btn-success", "yeşil"),
	("btn-danger", "kırmızı"),
	("btn-warning", "turuncu"),
	("btn-info", "açık mavi"),
	("btn-light", "ince beyaz"),
	("btn-dark", "koyu siyah"),
	("btn-white", "kalın beyaz"),
	("btn-link", "sadece mavi link"),

)

FONT_SIZE = (
	("8", 8),
	("10", 10),
    ("12", 12),
    ("14", 14),
    ("16", 16),
	("18", 18),
	("20", 20),
	("22", 22),
	("24", 24),
)

class Genel(models.Model):
	başlık = models.CharField(max_length= 100)
	slug = models.SlugField(unique=True, max_length=130)
	resim_grubu = models.ForeignKey(Resim, on_delete=models.CASCADE, blank = True , null = True, verbose_name = "Resim grubu", related_name= "resim_grubu")
	kısa_içerik = RichTextField()
	uzun_içerik = RichTextField()
	aktif = models.BooleanField("aktif mi", default = False)
	sira = models.PositiveIntegerField("Sıralama Sayısı", default = 0)
	
	class Meta:
		verbose_name = 'Genel-Konu'
		verbose_name_plural = 'Genel-Konular'
	
	def __str__(self):
		return self.başlık
	
	def get_absolute_url(self):
		return reverse('anasayfa:genel-detail', kwargs={'slug':self.slug})
	
class RenkFont(models.Model):
	isim = models.CharField(max_length= 50)
	body = models.CharField('komple sayfanın arka plan rengi', max_length=30, choices=ARKA_PLAN_RENKLERİ, blank = True)
	kategorilerim_yazı_rengi = models.CharField('KATEGORİLERİM başlığının yazı rengi', max_length=30, choices=FONT_RENKLERİ, blank = True)
	kategorilerim_yazısı_arka_plan_rengi = models.CharField('KATEGORİLERİM başlığının arka plan rengi', max_length=30, choices=ARKA_PLAN_RENKLERİ, blank = True)		
	kategorilerim_arka_plan_rengi = models.CharField('KATEGORİLERİM bölümünün arka plan rengi', max_length=30, choices=ARKA_PLAN_RENKLERİ, blank = True)	
	kategorilerim_yazı_boyutu = models.CharField('KATEGORİLERİM başlığının yazı büyüklğü', max_length=30, choices=FONT_SIZE, blank = True)	
	urunler_yazı_boyutu = models.CharField('Ürünler başlığının yazı büyüklğü', max_length=30, choices=FONT_SIZE, blank = True)	
	urunler_arka_plan_rengi = models.CharField('Ürünler başlığının arka plan rengi', max_length=30, choices=ARKA_PLAN_RENKLERİ, blank = True)	
	urunler_yazı_büyüklüğü = models.CharField('Ürün isimlerinin yazı büyüklğü', max_length=30, choices=FONT_SIZE, blank = True)
	ilk_üç_button = models.CharField("ürün kategorilerindeki ilk üç button'un rengi", max_length=30, choices=BUTTON_RENKLERİ, blank = True)
	dördüncü_button = models.CharField("ürün kategorilerindeki dördüncü button'un rengi", max_length=30, choices=BUTTON_RENKLERİ, blank = True)
	beşinci_button = models.CharField("ürün kategorilerindeki beşinci button'un rengi", max_length=30, choices=BUTTON_RENKLERİ, blank = True)
	altıncı_button = models.CharField("ürün kategorilerindeki altıncı button'un rengi", max_length=30, choices=BUTTON_RENKLERİ, blank = True)
	yedinci_button = models.CharField("ürün kategorilerindeki yedinci button'un rengi", max_length=30, choices=BUTTON_RENKLERİ, blank = True)
	sekizinci_button = models.CharField("ürün kategorilerindeki sekizinci button'un rengi", max_length=30, choices=BUTTON_RENKLERİ, blank = True)
	buttonlar_yazı_büyüklüğü = models.CharField('Kategori isimlerinin yazı büyüklğü', max_length=30, choices=FONT_SIZE, blank = True)
	isim = models.CharField(max_length= 50, default = "Site Geneli Özellikler")
	navbardaki_yazı = models.CharField("Navbardaki yazı", max_length= 250, default = "KİTAP OKUMA HEDEFİNİZE PLANLI ÇÖZÜM")
	site_adı = models.CharField("Sitenin Adı", max_length= 250, default = "Kitap Turnuvası")
	cep_telefonu = models.CharField("Cep Telefonu", max_length= 50, default = "0505 763 63 81")
	
	class Meta:
		verbose_name = 'Renk-ve-Yazı'
		verbose_name_plural = 'Renk-ve-Yazılar'
	
	def __str__(self):
		return self.isim
        
class Slayt(models.Model):
    isim = models.CharField("Başlık", max_length= 50, blank=True)
    yazı = models.CharField("Yazı", max_length= 200, blank=True)
    image = models.ImageField("resim", blank=True, null = True)
    aktif = models.BooleanField("Aktif mi?", help_text="Sitede görünmesini istiyorsanız işaretleyiniz!!!", default = False)
    sıralama_sayısı = models.PositiveIntegerField("Anasayfa Sıralama Sayısı", default = 0)

    def __str__(self):
        return self.isim

    class Meta:
        verbose_name = 'Slayt-Resmi'
        verbose_name_plural = 'Slayt-Resimleri'
        ordering = ['sıralama_sayısı']

class Yorum(models.Model):
    isim = models.CharField("Kullanıcı Adı:", max_length= 50)
    okul = models.CharField('Okulunuz:', max_length=30, choices= OKULLAR)
    content = models.TextField("Yorum:")
    aktif = models.BooleanField("Aktif mi?", help_text="Sitede görünmesini istiyorsanız işaretleyiniz!!!", default = False)
    created_at = models.DateTimeField("Oluşturulma tarihi", auto_now_add=True)
    
    class Meta:
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'
        ordering = ['-created_at',]

    def __str__(self):
        return self.isim
    
    def get_absolute_url(self):
        return reverse('anasayfa:ziyaret')

class Dokuman(models.Model):
    isim = models.CharField("Doküman Adı:", max_length= 50)
    slug = models.SlugField(unique=True, max_length=130)
    dokuman_ekle = models.FileField("doküman yükle")
    aktif = models.BooleanField("aktif mi", default = False)
    sira = models.PositiveIntegerField("Sıralama Sayısı", default = 0)
    
    class Meta:
        verbose_name = 'Doküman'
        verbose_name_plural = 'Dokümanlar'

    def __str__(self):
        return self.isim

    def get_absolute_url(self):
        return reverse('anasayfa:dokuman-detail', kwargs={'slug':self.slug})
    

	
