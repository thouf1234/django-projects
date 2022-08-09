from django.urls import path
from firstApp import views
urlpatterns = [
path('register/',views.studentform),
]
