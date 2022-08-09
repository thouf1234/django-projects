from django.shortcuts import render,redirect
from firstApp.models import employee_crud_fdv_model
from firstApp import forms
# Create your views here.
def retrieve_view(request):
    employee = employee_crud_fdv_model.objects.all()
    return render(request,'firstApp/retrieve.html',{'employee':employee})
def create_view(request):
    form=forms.employee_form()
    if request.method=='POST':
        form = forms.employee_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/index/retrieve')
    return render(request,'firstApp/create.html',{'form':form})
def delete_view(request,id):
    employee=employee_crud_fdv_model.objects.get(id=id)
    employee.delete()
    return redirect('/index/retrieve')
def update_view(request,id):
    employee=employee_crud_fdv_model.objects.get(id=id)
    if request.method=='POST':
        form = forms.employee_form(request.POST,instance=employee)# the employee instance record got at line no 21 si used here as instance to update an existing record and not to create new record
        if form.is_valid():
            form.save(commit=True)
            return redirect('/index/retrieve')
    return render(request,'firstApp/update.html',{'form':employee})
