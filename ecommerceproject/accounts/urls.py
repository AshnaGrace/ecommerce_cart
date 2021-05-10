from django.urls import path
app_name='accounts'
from accounts import views

urlpatterns = [
   path('register',views.register,name='register'),
   path('login',views.login,name='login'),
   path('logout',views.logout,name='logout')
    ]