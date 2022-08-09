from django.urls import path
from firstApp import views
urlpatterns = [
path('home/',views.home_view),
]
