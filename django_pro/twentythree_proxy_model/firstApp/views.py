from django.shortcuts import render
from firstApp.models import Employee,ProxyEmployee1,ProxyEmployee2
# Create your views here.
def Employee_view(request):
    employee=Employee.objects.all()
    return render(request,'firstApp/employee.html',{'employee':employee})
def ProxyEmployee1_view(request):
    employee=ProxyEmployee1.objects.all()
    return render(request,'firstApp/proxyemployee1.html',{'employee':employee})
def ProxyEmployee2_view(request):
    employee=ProxyEmployee2.objects.all()
    return render(request,'firstApp/proxyemployee2.html',{'employee':employee})
