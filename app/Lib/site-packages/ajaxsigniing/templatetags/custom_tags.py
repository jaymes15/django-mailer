from django import template
register = template.Library()

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

@register.inclusion_tag('ajaxsigniing/signup.html')
def sign_up():
	form_class = UserCreationForm
	return {'form': form_class}