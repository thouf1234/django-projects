from django.shortcuts import render
from . import forms
from . import models
# Create your views here.
def movie_home(request):
    return render(request,'firstApp/home.html')
def movie_add(request):
    form = forms.movie_form()
    if request.method=='POST':
        form = forms.movie_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return movie_home(request)
    return render(request,'firstApp/movie_add.html',{'form':form})
def movie_view(request):
    movies = models.movie_model.objects.all().order_by('rating')
    movie_dict = {'movie':movies}
    return render(request,'firstApp/movie_view.html',context=movie_dict)
