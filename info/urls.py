from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
	path('' , views.Index , name='index'),
	path('info/', views.Info.as_view(), name='info'),
	path('dori/<str:drug_slug>/', views.DrugDetail.as_view(), name='maindori_detail'),
	path('results/', views.FilterDrugsView.as_view(), name='search_result'),
	path('category/<str:category_slug>', views.CategoryDrugsView.as_view(), name='category_view'),
]