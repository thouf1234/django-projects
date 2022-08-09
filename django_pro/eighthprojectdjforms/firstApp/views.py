from django.shortcuts import render
from . import forms
# Create your views here.
def studentform(request):
    if request.method =='GET':
        form = forms.studentsregister()
    if request.method =='POST':
        form = forms.studentsregister(request.POST)
        if form.is_valid():
            print("form validation completed and submitted successfully")
            print("student name :",form.cleaned_data['name'])
            print("student rollno :",form.cleaned_data['rollno'])
            print("student email :",form.cleaned_data['email'])
            print("student password :",form.cleaned_data['password'])
            print("student repassword :",form.cleaned_data['repassword'])
            print("student feedback :",form.cleaned_data['feedback'])
            my_dict={'name':form.cleaned_data['name'],'rollno':form.cleaned_data['rollno'],'email':form.cleaned_data['email'],'feedback':form.cleaned_data['feedback']}
            return render(request,'firstApp/thankyou.html',context=my_dict)
    return render(request,'firstApp/register.html',{'form':form})
