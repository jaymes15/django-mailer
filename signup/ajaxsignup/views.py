from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegistrationForm, EmailForm

# Create your views here.

def home(request):
	return render(request,'ajaxsignup/home.html')


def firstlogin(request):
	#send_mail(subject, message, from_email, to_list, fail_silently = True)
	
	if request.method =='POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#Log user in
			user = form.get_user()
			login(request,user)
			subject = 'thank you for signing up'
			message = 'welcome to the new community'
			from_email = settings.EMAIL_HOST_USER
			print(user.email)
			to_list = [user.email]
			send_mail(subject,message,from_email,to_list,fail_silently = False)
			return redirect('ajaxsignup:home')



	else:
		form = AuthenticationForm()
	return render(request,'ajaxsignup/login.html',{'form':form})
	
	
	return render(request,'ajaxsignup/sendmail.html')


def sendmail(request):
	user = User.objects.values_list('email', flat=True)
	
	if request.method == 'POST':
		form = EmailForm(request.POST)
		if form.is_valid():
			mail = form.save(commit=False)
			mail.user = request.user
			from_email = settings.EMAIL_HOST_USER
			to_list = user
			send_mail(mail.subject,mail.message,from_email,to_list,fail_silently = False)

			mail.save()
			return redirect('ajaxsignup:home')
	else:
		form = EmailForm()
		
	return render(request,'ajaxsignup/sendmail.html',{'form':form})
	

def signup_view(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			
			return redirect('ajaxsignup:firstlogin')
	else:
		form = RegistrationForm()
		
	return render(request,'ajaxsignup/signup.html',{'form':form})

def login_view(request):
	if request.method =='POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#Log user in
			user = form.get_user()
			login(request,user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:	

				return redirect('ajaxsignup:home')



	else:
		form = AuthenticationForm()
	return render(request,'ajaxsignup/login.html',{'form':form})
	
def logout_view(request):
	if request.method =='POST':
		logout(request)
		return redirect('ajaxsignup:login')	