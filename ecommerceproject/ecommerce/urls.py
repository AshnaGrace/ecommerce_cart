from django.urls import path
app_name='ecommerce'
from ecommerce import views

urlpatterns=[
    path('',views.allCat,name="allCat"),
    path('<slug:c_slug>/',views.allCat,name="probycat"),
    path('<slug:c_slug>/<slug:product_slug>/',views.proddetail,name="proddetail")
]

