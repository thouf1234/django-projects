from django.shortcuts import render
from firstApp.models import Employee
# Create your views here.
def Employee_view(request):
    #employee=Employee.objects.all()#note we can't have two model manager at a time
    #employee=Employee.objects.get_emp_sal_range(12000,17000)
    #employee=Employee.objects.get_emp_sorted_by('ename')
    return render(request,'firstApp/employee.html',{'employee':employee})
