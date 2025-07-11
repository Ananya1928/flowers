"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include

# Added by VBhat on 15/04/2024
from django.views.generic import TemplateView # useful in displaying index.html template
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('orders.urls')),
    path('', include('payments.urls')), 
    path('', include('accounts.urls')),
    path('', include('products.urls')),
    
    #path('api/', include('location.urls')),
    #path('', include('testapp.urls')),
    #path('', include('weather.urls')),

]
