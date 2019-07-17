from django.contrib import admin

from .models import Genel, RenkFont, Slayt, Yorum, Dokuman

class GenelAdmin(admin.ModelAdmin):
    list_display = ['başlık', 'resim_grubu',]
    prepopulated_fields = {'slug': ('başlık',)}
   
class SlaytAdmin(admin.ModelAdmin):
    list_display = ['isim', 'yazı', 'image', 'aktif', 'sıralama_sayısı']
    list_editable = ['yazı', 'image', 'aktif', 'sıralama_sayısı']

class YorumAdmin(admin.ModelAdmin):
    list_display = ['isim', 'content', 'aktif',]
    list_editable = ['content', 'aktif',]

class DokumanAdmin(admin.ModelAdmin):
    list_display = ['isim', 'slug', 'dokuman_ekle']
    prepopulated_fields = {'slug': ('isim',)}
    list_editable = ['slug', 'dokuman_ekle']

admin.site.register(Dokuman, DokumanAdmin)
admin.site.register(Yorum, YorumAdmin)
admin.site.register(Slayt, SlaytAdmin)
admin.site.register(Genel, GenelAdmin)
admin.site.register(RenkFont)
