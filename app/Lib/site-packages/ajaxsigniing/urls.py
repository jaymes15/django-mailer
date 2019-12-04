from django.conf.urls import url
from . import views
from django.urls import path

app_name= 'ajaxsigniing'
urlpatterns = [
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),   
]