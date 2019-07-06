from django.contrib import admin

from .models import Genel, RenkFont

class GenelAdmin(admin.ModelAdmin):
    list_display = ['başlık', 'image',]
    prepopulated_fields = {'slug': ('başlık',)}


admin.site.register(Genel, GenelAdmin)
admin.site.register(RenkFont)
