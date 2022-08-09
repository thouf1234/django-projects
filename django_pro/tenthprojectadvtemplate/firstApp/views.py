from django.shortcuts import render

# Create your views here.
def basetemplate(request):
    return render(request,'firstApp/base.html')
def homepage(request):
    return render(request,'firstApp/home.html')
def moviespage(request):
    return render(request,'firstApp/movies.html')
def politicspage(request):
    return render(request,'firstApp/politics.html')
def sportspage(request):
    return render(request,'firstApp/sports.html')
