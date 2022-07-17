from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {'slug':('name',)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {'slug':('name',)}


@admin.register(MainDori)
class MainDoriAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    list_filter = ('producer', 'name')
    prepopulated_fields = {
    'slug':('name',)
    }