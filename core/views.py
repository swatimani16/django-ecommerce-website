from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView, DetailView
from .models import Item, Order, OrderItem
from django.utils import timezone
from django.contrib import messages



# Create your views here.

def item_list(request):
    context = {
        'items' : Item.objects.all()
    }
    return render(request,"core/home-page.html",context)

class HomeView(ListView):
    model = Item
    template_name = "core/home-page.html"

def checkout(request):
    return render(request,"core/checkout-page.html")


# def products(request):
#     context = {
#         'items' : Item.objects.all()
#     }
#     return render(request,"core/product-page.html",context)

class ItemDetailView(DetailView): 
    model = Item
    template_name = "core/product.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug = slug)
    order_item, created = OrderItem.objects.get_or_create(item = item, user = request.user, ordered = False)
    order_qs = Order.objects.filter(user = request.user, ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.item.filter(item__slug = item.slug).exists():
            order_item.quantity+=1
            order_item.save()
            messages.info(request,"This item quantity was updated into your cart!")
            return redirect("products",slug = slug)
        else:
            messages.info(request,"This item was added to your cart!")
            order.item.add(order_item)
            return redirect("products",slug = slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user = request.user, order_date = ordered_date)
        order.item.add(order_item)
        messages.info(request,"This item was added to your cart!")
        return redirect("products",slug = slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
    user = request.user,
     ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.item.filter(item__slug = item.slug).exists():
            order_item = OrderItem.objects.filter(item = item, user = request.user, ordered = False)[0]
            order.item.remove(order_item)
            messages.info(request,"This item was removed from your cart!")
            return redirect("products",slug = slug)

        else:
            messages.info(request,"This item was not inyour cart!")
            return redirect("products",slug = slug)
    else:
        messages.info(request,"You do not have an active order")
        return redirect("products",slug = slug)
    