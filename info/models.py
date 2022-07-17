from django.db import models
from datetime import datetime
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	name = models.CharField('Kategoriya nomi', max_length=50)
	nameru = models.CharField("Kategoriya nomi ruscha", max_length=50)
	slug = models.SlugField('*', unique=True, max_length=50)
	image = models.ImageField("rasm",upload_to = 'category_photo/')
	desc = models.TextField('Kategoriya haqida', blank=True, max_length=1500)
	descru = models.TextField('Kategoriya haqida ruscha', blank=True, max_length=1500)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Kategoriya'
		verbose_name_plural = 'Kategoriyalar'

	def get_absolute_url(self):
		return reverse('info:category_view',kwargs={'category_slug':self.slug})

class SubCategory(models.Model):
	name = models.CharField('SubKategoriya nomi', max_length=100)
	nameru = models.CharField('SubKategoriya nomi ruscha', max_length=100)
	slug = models.SlugField('*', unique=True, max_length=10)
	category = models.ManyToManyField(Category)
	image = models.ImageField("rasm",upload_to = 'sub_category_photo/')
	desc = models.TextField('Kategoriya haqida', blank=True, max_length=1500)
	descru = models.TextField('Kategoriya haqida ruscha', blank=True, max_length=1500)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'SubKategoriya'
		verbose_name_plural = 'SubKategoriyalar'

	def get_absolute_url(self):
		return reverse('info:sub_category_view',kwargs={'sub_category_slug':self.slug})

class MainDori(models.Model):
	name = models.CharField('Preparatning savdo nomi ya\'ni nomi:',max_length=500)
	nameru = models.CharField('Ruscha Preparatning savdo nomi ya\'ni nomi ruscha :',max_length=500)
	image = models.ImageField("rasm",upload_to = 'info_photo/')
	slug = models.SlugField('*',unique=True,max_length=50)
	affective_stuff = RichTextField('Ta\'sir etuvchi moddalar:')
	affective_stuffru = RichTextField('Ruscha: Ta\'sir etuvchi moddalar:')
	size_of_drug = RichTextField('Dori shakli:')
	size_of_drugru = RichTextField('Ruscha: Dori shakli:')
	ingredients = RichTextField('Tarkibi:')
	ingredientsru = RichTextField('Ruscha: Tarkibi:')
	describtion = RichTextField('Ta\'rifi:')
	describtionru = RichTextField('Ruscha: Ta\'rifi:')
	what_can_drug_do = RichTextField('Farmakoterapeftik guruhi:')
	what_can_drug_doru = RichTextField('Ruscha: Farmakoterapeftik guruhi:')
	code_atx = models.CharField('Kod ATX:',max_length=50)
	category = models.ForeignKey(Category, verbose_name='Kategoriya', on_delete=models.SET_NULL, null=True)
	subcategory = models.ManyToManyField(SubCategory)
	#### FULL DESCRIBTION Farmakalogik xususiyati ####
	far_desc = RichTextField("Farmakalogik xususiyati:")
	far_descru = RichTextField("Ruscha: Farmakalogik xususiyati:")

	# Qo'llanishi
	using = RichTextField("Qo'llanishi:")
	usingru = RichTextField("Ruscha: Qo'llanishi:")

	# Nojo'ya ta'siri
	bad_side = RichTextField("Nojo'ya ta'siri:")
	bad_sideru = RichTextField("Ruscha: Nojo'ya ta'siri:")

	# Qollash mumkin bolmagan holatlar
	non_use = RichTextField("Qo\'llash mumkin bo'lmagan holatlar:")
	non_useru = RichTextField("Ruscha: Qo\'llash mumkin bo'lmagan holatlar:")

	# Dorilarning ozaro tasiri
	react_drugs = RichTextField("Dorilarning o'zaro ta'siri:")
	react_drugsru = RichTextField("Ruscha: Dorilarning o'zaro ta'siri:")

	# Maxsus korsatmalar
	spec_direct = RichTextField("Maxsus korsatmalar:")
	spec_directru = RichTextField("Ruscha: Maxsus korsatmalar:")

	# Chiqarilish shakli
	prod_drug = RichTextField("Chiqarilish shakli:")
	prod_drugru = RichTextField("Ruscha: Chiqarilish shakli:")

	# Saqlash sharoiti
	keep = RichTextField("Saqlash sharoiti:")
	keepru = RichTextField("Ruscha: Saqlash sharoiti:")

	# Yaroqlilik muddati
	shelf_life = RichTextField("Yaroqlilik muddati:")
	shelf_liferu = RichTextField("Ruscha: Yaroqlilik muddati:")

	# Dorixonalarda berilish tartibi
	give = RichTextField("Dorixonalarda berilish tartibi:")
	giveru = RichTextField("Ruscha: Dorixonalarda berilish tartibi:")

	# Ishlab chiqaruvchi
	producer = RichTextField("Ishlab chiqaruvchi:")
	producerru = RichTextField("Ruscha: Ishlab chiqaruvchi:")
	date = models.DateTimeField('post sanasi', auto_now_add=True)

	class Meta:
		verbose_name = 'Dori'
		verbose_name_plural = 'Dorilar'

	def __str__(self):
		return self.name

	def get_dori(self):
		return reverse('info:maindori_detail', kwargs={'drug_slug':self.slug})


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField(auto_now_add=True)
	post = models.ForeignKey('MainDori',on_delete=models.CASCADE)
	content = models.TextField()

	def __str__(self):
		return slef.user.username
