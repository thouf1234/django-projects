from django.urls import path
from firstApp import views
urlpatterns = [
    path('base/', views.basetemplate),
    path('home/', views.homepage),
    path('movies/', views.moviespage),
    path('sports/', views.sportspage),
    path('politics/', views.politicspage),
    ]
