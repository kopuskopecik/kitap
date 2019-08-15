from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
	url(r'^siparislerim/$', views.siparislerim, name='siparisler'),
	url(r'^siparisler/$', views.tum_siparisler, name='siparislerin_hepsi'),
	path('istatistikler/', views.istatistikler, name='istatistikler'),
	path('istatistikler/<int:gun>/', views.istatistik, name='istatistik'),
	url(r'^siparis-ekle/$', views.siparis_ekle, name='siparis-ekle'),
	path('<int:id>/siparisi-duzenle/', views.siparis_duzenle, name="siparis-duzenle"),
	path('<int:id>/', views.siparis_detail, name="siparis-detail"),
	path('<int:id>/urun-ekle/', views.siparis_detail_urun_ekle, name="siparis-detail-urun-ekle"),
	
]