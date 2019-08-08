from django.shortcuts import render, redirect, HttpResponse
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

from .models import Genel, RenkFont, Slayt, Yorum, Dokuman

from shop.models import Category, Product, AnaCategory


class AnaSayfa(generic.ListView):
	model = AnaCategory
	template_name = 'anasayfa/anasayfa.html'
	ordering = ('sıralama_sayısı',)
	context_object_name = "ana_kategoriler"
	queryset = AnaCategory.objects.filter(aktif = True)
	
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		urunler = Product.objects.filter(anasayfada_gosterilsin_mi = True).order_by('sıralama_sayısı')
		genel = Genel.objects.filter(aktif = True )
		slaytlar = Slayt.objects.filter(aktif = True)
		if slaytlar:
			ilk_slayt = slaytlar[0]
			diger_slaytlar = slaytlar[1:]
			context["ilk_slayt"] = ilk_slayt
			context["diger_slaytlar"] = diger_slaytlar
		context["urunler"] = urunler
		context["genel"] = genel
		return context
	

class GenelDetailView(generic.DetailView):
	model = Genel
	template_name = 'anasayfa/genel-detail.html'
	ordering = ('sira',)
	queryset = Genel.objects.filter(aktif = True)

class ZiyaretView(SuccessMessageMixin, generic.CreateView):
	model = Yorum
	template_name = 'anasayfa/ziyaret.html'
	fields = ['isim', 'okul', 'content']
	success_message = "Mesajınız iletilmiştir. Teşekkürler."
    
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		yorumlar = Yorum.objects.filter(aktif = True)
		context["yorumlar"] = yorumlar
		return context

class DokumanListView(generic.ListView):
	model = Dokuman
	template_name = 'anasayfa/dokumanlar.html'
	context_object_name = "dokumanlar"
	ordering = ('sira',)
	queryset = Dokuman.objects.filter(aktif = True)

class YasalView(generic.TemplateView):
	template_name = 'anasayfa/yasal.html'

class IletisimView(generic.TemplateView):
    template_name = 'anasayfa/iletisim.html'

def deneme(request):

    file_path = 'templates/a.docx'
    with open(file_path,'rb') as doc:
        response = HttpResponse(doc.read(), content_type='application/ms-word')
        # response = HttpResponse(template_output)
        response['Content-Disposition'] = 'attachment;filename=name.docx'
        return response
    