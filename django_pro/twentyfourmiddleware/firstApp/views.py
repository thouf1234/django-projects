from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request):
    print("this line is printed by view function while processing request")
    #div=10/0
    return HttpResponse('<h1>custome middleware demo</h1>')
