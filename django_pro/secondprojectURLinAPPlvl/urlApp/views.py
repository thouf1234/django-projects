from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def chennai(request):
    s = '<h1>chennai has the perfect climate</h1>'
    return HttpResponse(s)
def ooty(request):
    s = '<h1>ooty is chill/h1>'
    return HttpResponse(s)
def mysore(request):
    s = '<h1>mysore have best sweets</h1>'
    return HttpResponse(s)
