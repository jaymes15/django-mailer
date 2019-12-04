from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Emailinfo






class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True,widget=forms.TextInput(
	        	attrs={
	        			'class':'form-control',


	        	}))

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'
			) 
	def save(self,commit = True):
		user = super(RegistrationForm,self).save(commit = False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()



class EmailForm(forms.ModelForm):

	        subject = forms.CharField(widget=forms.TextInput(
	        	attrs={
	        			'class':'form-control',


	        	}))
	        '''
	        slug = forms.SlugField(widget=forms.TextInput(
	        	attrs={
	        			'class':'form-control',
	        	}))
	        	'''
	        message =  forms.CharField(widget=forms.Textarea(
	        	attrs={
	        			'class':'form-control',


	        	}))
	        
	        class Meta:
	        	model = Emailinfo
	        	exclude = ['created_on','user']			