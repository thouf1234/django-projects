from django.shortcuts import render
from firstApp import forms
# Create your views here.
def DjformCreative_view(request):
    form=forms.DjformCreative()
    if request.method =='GET':
        return render(request,'firstApp/display.html',{'form':form})
    if request.method =='POST':
        form=forms.DjformCreative(request.POST)
        if form.is_valid():
            return render(request,'firstApp/result.html',{'form':form})
