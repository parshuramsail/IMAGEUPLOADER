from django.shortcuts import render
from .models import Image,Category

# Create your views here.
def home_page(request):
    cats=Category.objects.all()
    images=Image.objects.all()
    return render(request,'appy/home.html',{'images':images,'cats':cats})

def category_page(request,id):
    cats=Category.objects.all()
    category=Category.objects.get(pk=id)
    images=Image.objects.filter(cat=category)
    return render(request,'appy/home.html',{'images':images,'cats':cats})

def about_us(request):
    return render(request,'appy/about.html')

