from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def greet(request):
    if int(str(datetime.datetime.now()).split()[1].split(":")[0])>=0 and int(str(datetime.datetime.now()).split()[1].split(":")[0])<12:
        s = "<h1>good morning!! the date and time of the server is : "+str(datetime.datetime.now())
        return HttpResponse(s)
    elif int(str(datetime.datetime.now()).split()[1].split(":")[0])>=12 and int(str(datetime.datetime.now()).split()[1].split(":")[0])<=20:
        s = "<h1>good evening!! the date and time of the server is : "+str(datetime.datetime.now())
        return HttpResponse(s)
    elif int(str(datetime.datetime.now()).split()[1].split(":")[0])>=21 and int(str(datetime.datetime.now()).split()[1].split(":")[0])<=23:
        s = "<h1>good night!! the date and time of the server is : "+str(datetime.datetime.now())
        return HttpResponse(s)
def chennaijob(request):
    s = "<h1>this is the chennai job vaccancy detail</h1>"
    return HttpResponse(s)
def hyderabadjob(request):
    s = "<h1>this is the hyderabad job vaccancy detail</h1>"
    return HttpResponse(s)
