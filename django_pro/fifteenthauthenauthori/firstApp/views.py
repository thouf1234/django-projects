from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms
from django.http import HttpResponseRedirect
# Create your views here.
def home_view(request):
    return render(request,'firstApp/home.html')
@login_required
def java_view(request):
    return render(request,'firstApp/java.html')
@login_required
def python_view(request):
    return render(request,'firstApp/python.html')
@login_required
def apptitude_view(request):
    return render(request,'firstApp/apptitude.html')
def logout_view(request):
    return render(request,'firstApp/logout.html')
def signup_view(request):
    form = forms.signup_form()
    if request.method=='POST':
        form = forms.signup_form(request.POST)
        user=form.save(commit=True)#django always expect the password in signup form to be encrypted and if not it wont consider that signup entry using set_password() method with the user entered password will encypted by django using default encryption
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'firstApp/signup.html',{'form':form})
