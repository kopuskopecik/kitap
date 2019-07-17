from django.contrib import admin
from .models import Category, Product, Resim, AnaCategory, TekliResim

class ProductInline(admin.StackedInline):
	model = Product

	
class AnaCategoryAdmin(admin.ModelAdmin):
		
	list_display = ['name', 'slug','sayfa_durumu', 'bireysel_mi','sadece_madalyalı_mı', 'sıralama_sayısı', 'aktif', ]
	list_editable = ['slug','sayfa_durumu', 'bireysel_mi','sadece_madalyalı_mı', 'sıralama_sayısı', 'aktif',]
	list_filter = ['name', ]
	prepopulated_fields = {'slug': ('name',)}

	
class CategoryAdmin(admin.ModelAdmin):
		
	list_display = ['name', 'ana_kategori', 'sayi', 'image1', 'nasıl_uygulanır_resimleri', 'odul_buttonu_resimleri', 'madalyalı_mı', 'sayfa_sayısı','aktif']
	list_editable = ['ana_kategori', 'sayi', 'image1', 'nasıl_uygulanır_resimleri', 'odul_buttonu_resimleri', 'madalyalı_mı', 'sayfa_sayısı','aktif']
	prepopulated_fields = {'slug': ('name',)}
	list_filter = ['ana_kategori', 'aktif']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'anasayfada_gosterilsin_mi', 'sıralama_sayısı', 'price', 'agırlık', 'ogrenci_sayisi','aktif']
    list_editable = ['category', 'anasayfada_gosterilsin_mi', 'sıralama_sayısı','price', 'agırlık', 'ogrenci_sayisi', 'aktif']
    list_filter = ['category', 'category__ana_kategori', 'sıralama_sayısı','anasayfada_gosterilsin_mi', 'aktif']
    prepopulated_fields = {'slug': ('name',)}


class ResimAdmin(admin.ModelAdmin):
    list_display = ['isim', 'resimler', ]
    list_editable = ['resimler', ]
    list_filter = ['isim',]

class TekliResimAdmin(admin.ModelAdmin):
    list_display = ['isim', 'image1', ]
    list_editable = ['image1', ]
    list_filter = ['isim',]

admin.site.register(AnaCategory, AnaCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(TekliResim)
admin.site.register(Resim)


