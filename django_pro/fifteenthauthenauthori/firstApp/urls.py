from django.urls import path
from firstApp import views
urlpatterns = [
    path('home/', views.home_view),
    path('java/', views.java_view),
    path('python/', views.python_view),
    path('apptitude/', views.apptitude_view),
    path('logout/',views.logout_view),
    path('signup/',views.signup_view),
    ]
