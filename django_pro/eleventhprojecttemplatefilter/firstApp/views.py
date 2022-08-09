from django.shortcuts import render
from firstApp.models import filter_model
# Create your views here.
def upper_view(request):
    data = filter_model.objects.all()
    my_dict={'data':data}
    return render(request,'firstApp/upper.html',context=my_dict)
def lower_view(request):
    data = filter_model.objects.all()
    my_dict={'data':data}
    return render(request,'firstApp/lower.html',context=my_dict)
def title_view(request):
    data = filter_model.objects.all()
    my_dict={'data':data}
    return render(request,'firstApp/title.html',context=my_dict)
def date_filter_argument_view(request):
    data = filter_model.objects.all()
    my_dict={'data':data}
    return render(request,'firstApp/date_filter_arguments.html',context=my_dict)
def add_sufix_view(request):
    data = filter_model.objects.all()
    my_dict={'data':data}
    return render(request,'firstApp/add_sufix.html',context=my_dict)
def timesince_view(request):
    data = filter_model.objects.all()
    my_dict={'data':data}
    return render(request,'firstApp/date_time_since.html',context=my_dict)
def cust_filter_slice(request):
    data = filter_model.objects.all()
    my_dict={'data':data}
    return render(request,'firstApp/custom_filter.html',context=my_dict)
