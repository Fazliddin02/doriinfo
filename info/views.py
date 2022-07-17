from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse,JsonResponse
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.utils.translation import gettext as _
from django.utils.translation import get_language,activate,gettext
from django.views.generic.base import View
from .forms import CommentForm
from django.views.generic import ListView,DetailView
from django.db.models import Q
from django.core.paginator import Paginator
cur_language = get_language()
# Create your views here.
def Index(request):
	category = Category.objects.all()
	dori = MainDori.objects.all().order_by('-date')[:8]

	context = {
	'cat':category,
	'dori':dori,
	}

	return render(request,"index.html",context)


class Info(View):
	def get(self, request):
		dori = MainDori.objects.all().order_by('date')
		category = Category.objects.all()

		paginator = Paginator(dori, 4) # Show 2 movies per page.
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)

		context = {
		'dori':dori,
		'cat':category,
		}
		return render(request, 'blog-grid.html',context)

class DrugDetail(View):
	def get(self, request, drug_slug):

		drug = get_object_or_404(MainDori,slug=drug_slug)
		category = Category.objects.all()

		context = {
		'dori':drug,
		'cat':category,

		}
		return render(request, 'blog-single.html', context)


class FilterDrugsView(ListView):
	#Filter inDori
	model = MainDori
	template_name = 'list.html'
	
	def get_queryset(self): # new 
		query = self.request.GET.get('q')
		object_list = MainDori.objects.filter(
			Q(name__icontains=query) | Q(nameru__icontains=query)| Q(describtion__icontains=query)| Q(describtionru__icontains=query)
		)

		return object_list

class CategoryDrugsView(ListView):
	# Category Movies View
	def get(self, request, category_slug):
		category = Category.objects.get(slug=category_slug)
		drugs = category.maindori_set.all()

		paginator = Paginator(drugs, 4) # Show 2 movies per page.
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)

		context = {'category_drug':drugs, 'drugs':page_obj}
		return render(request, 'categories_list.html', context)