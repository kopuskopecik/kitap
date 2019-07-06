from django.shortcuts import render, redirect
from django.views import generic

from .models import Genel, RenkFont

from shop.models import Category, Product, AnaCategory


class AnaSayfa(generic.ListView):
	model = AnaCategory
	template_name = 'anasayfa/anasayfa.html'
	ordering = ('sıralama_sayısı',)
	context_object_name = "ana_kategoriler"
	queryset = AnaCategory.objects.filter(aktif = True)
	
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		urunler = Product.objects.filter(anasayfada_gosterilsin_mi = True)
		urunler1 = urunler[0:2]
		urunler2 = urunler[2:]
		genel = Genel.objects.all()
		context["urunler1"] = urunler1
		context["urunler2"] = urunler2
		context["genel"] = genel
		return context
	

class GenelDetailView(generic.DetailView):
	model = Genel
	template_name = 'anasayfa/genel-detail.html'