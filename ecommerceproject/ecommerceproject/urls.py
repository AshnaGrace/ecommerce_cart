"""ecommerceproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ecommerce import views
from ecommerceproject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecommerce/',include(('ecommerce.urls'),namespace='ecommerce')),
    path('search/',include(('searchapp.urls'),namespace='searchapp')),
    path('cart/',include('cart.urls')),
   path('accounts/',include(('accounts.urls'),namespace='accounts')),
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)