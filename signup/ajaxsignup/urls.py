from django.urls import path
from . import views



app_name= 'ajaxsignup'
urlpatterns = [
    path('', views.home,name='home'),
    path('sendmail/', views.sendmail,name='sendmail'),
    path('signup/', views.signup_view,name='register'),
    path('signin/', views.firstlogin,name='firstlogin'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
    
]