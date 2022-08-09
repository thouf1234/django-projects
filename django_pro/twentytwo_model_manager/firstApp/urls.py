from django.urls import path
from firstApp import views
urlpatterns = [
    path('employee/',views.Employee_view),
    ]
