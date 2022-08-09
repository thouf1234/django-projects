from django.shortcuts import render
from firstApp.models import Student,Teacher
# Create your views here.
def Student_view(request):
    student=Student.objects.all()
    return render(request,'firstApp/student.html',{'student':student})
def Teacher_view(request):
    teacher=Teacher.objects.all()
    return render(request,'firstApp/teacher.html',{'teacher':teacher})
