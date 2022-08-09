from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def secwelcome(request):
    s = "<h1>this is the welcome message from 2nd application</h1>"
    return HttpResponse(s)
    
