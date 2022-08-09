from django.shortcuts import render
from firstApp import forms
# Create your views here.
def pageno_session_view(request):
    count=request.session.get('count',0)
    new_count=count+1
    request.session['count']=new_count
    print(request.session.set_expiry(10))
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    return render(request,'firsTApp/pageno.html',{'count':new_count})
def session_form_name_view(request):
    form=forms.session_forms_name()
    return render(request,'firstApp/name_form.html',{'form':form})
def session_form_age_view(request):
    name=request.GET['name']
    request.session['name']=name
    form=forms.session_forms_age()
    return render(request,'firstApp/age_form.html',{'form':form})
def session_form_gf_view(request):
    age=request.GET['age']
    request.session['age']=age
    form=forms.session_forms_gf()
    return render(request,'firstApp/gf_form.html',{'form':form})
def session_form_result_view(request):
    gf=request.GET['gf']
    request.session['gf']=gf
    return render(request,'firstApp/result_form.html')
