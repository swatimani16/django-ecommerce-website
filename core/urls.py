from django.urls import path,include
from .views import item_list, HomeView, ItemDetailView, checkout,add_to_cart,remove_from_cart


urlpatterns = [
    path('',HomeView.as_view(),name = 'item-list'),
    path('checkout/',checkout,name = 'checkout'),
    path('products/<slug>/',ItemDetailView.as_view(),name = 'products'),
    path('add-to-cart/<slug>/',add_to_cart,name = 'add-to-cart'),
    path('remove_from_cart/<slug>/',remove_from_cart,name = 'remove_from_cart'),
]