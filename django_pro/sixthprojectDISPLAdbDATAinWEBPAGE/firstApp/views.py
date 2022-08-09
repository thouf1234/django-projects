from django.shortcuts import render
from firstApp.models import employee
# Create your views here.
def empview(request):
    emp_list = employee.objects.all()
    emp_dict = {'emp_info':emp_list}
    return render(request,'firstApp/home.html', context = emp_dict)
