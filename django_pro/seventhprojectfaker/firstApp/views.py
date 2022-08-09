from django.shortcuts import render
from firstApp.models import chennai,hyderabad,delhi
# Create your views here.
def indexview(request):
    return render(request,'firstApp/home.html')
def chennaiview(request):
    chennaiviewsdata = chennai.objects.order_by('date')
    my_dict = {'chennaiviewsdata': chennaiviewsdata}
    return render(request,'firstApp/chen.html',context= my_dict)
def hyderabadview(request):
    hyderabadviewsdata = hyderabad.objects.order_by('date')
    my_dict = {'hyderabadviewsdata': hyderabadviewsdata}
    return render(request,'firstApp/hyd.html',context= my_dict)
def delhiview(request):
    delhiviewsdata = delhi.objects.order_by('date')
    my_dict = {'delhiviewsdata': delhiviewsdata}
    return render(request,'firstApp/del.html',context= my_dict)
