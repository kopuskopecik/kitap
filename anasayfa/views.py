from django.shortcuts import render, redirect
from django.views import generic

from shop.models import Category


class AnaSayfa(generic.ListView):
	model = Category
	template_name = 'anasayfa/anasayfa.html'
	
	# def get(self, request, *args, **kwargs):
	# 	if request.user.is_authenticated:
	# 		if request.user.is_teacher:
	# 			return redirect('turnuva:ogretmen', request.user.teacher.pk)
	# 		else:
	# 			return redirect('my_account')
	# 	return super().get(request, *args, **kwargs)

#class DetailView(generic.DetailView):
#    model = Question
#    template_name = 'polls/detail.html'