from django.shortcuts import render
from .models import Item
# Create your views here.

def item_list(request):
    context = {
        'items' : Item.objects.all()
    }
    return render(request,"core/home-page.html",context)

def checkout(request):
    return render(request,"core/checkout-page.html")