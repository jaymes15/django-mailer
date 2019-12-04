from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Emailinfo(models.Model):
	        subject = models.CharField(max_length=100)
	        message = models.TextField()
	        created_on = models.DateTimeField(auto_now_add=True)
	        user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
	        