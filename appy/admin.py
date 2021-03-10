from django.contrib import admin
from .models import Category,Image

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','description')
    

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display=('title','description','image','added_date','cat')