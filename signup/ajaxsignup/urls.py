from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf.urls import url
from django.urls import path, include
from . import views



app_name= 'ajaxsignup'
urlpatterns = [
    path('', views.home,name='home'),
    path('sendmail/', views.sendmail,name='sendmail'),
    path('signup/', views.signup_view,name='register'),
    path('signin/', views.firstlogin,name='firstlogin'),
    path('login/', views.login_view,name='login'),
    path('accounts/login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
    url('^reset-password/$', PasswordResetView.as_view(), name='reset_password'),
    url('^reset-password/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password/done',PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    
]