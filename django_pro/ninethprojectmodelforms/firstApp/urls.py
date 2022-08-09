from django.urls import path
from firstApp import views
urlpatterns = [
path('home/',views.movie_home),
path('addmovie/',views.movie_add),
path('viewmovie/',views.movie_view),
]
