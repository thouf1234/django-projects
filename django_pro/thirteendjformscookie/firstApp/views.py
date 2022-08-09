from django.shortcuts import render
from firstApp import forms
# Create your views here.
def home_view(request):
    return render(request,'firstApp/home.html')
def Djform_view(request):
    form=forms.Djform()
    response=render(request,'firstApp/form.html',{'form':form})
    if request.method =='POST':
        form=forms.Djform(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            rollno=form.cleaned_data['rollno']
            email=form.cleaned_data['email']
            response.set_cookie('name',name)
            response.set_cookie('rollno',rollno)
            response.set_cookie('email',email)
    return response
def view_view(request):
    return render(request,'firstApp/view.html')
