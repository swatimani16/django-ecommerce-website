"""ecommerce_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user import views as user_views
from django.contrib.auth import views as auth_views
from core import views as core_views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/',include('allauth.urls')),
    path('',include('core.urls'), name = 'core'),
    path('register/', user_views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = "user/login.html"),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = "user/logout.html"),name='logout'),
    path('account/',user_views.account,name = 'account'),
    path('deals/',user_views.deals,name = 'deals'),
     path('clothes/',user_views.clothes,name = 'clothes'),
     path('shoes/',user_views.shoes,name = 'shoes'),
     path('help/',user_views.help,name = 'help'),
     path('checkout/',core_views.checkout,name = 'checkout'),
     path('products/',core_views.products,name = 'products'),
]

