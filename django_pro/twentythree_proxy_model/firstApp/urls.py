from django.urls import path
from firstApp import views
urlpatterns = [
    path('employee/',views.Employee_view),
    path('proxyemployee1/',views.ProxyEmployee1_view),
    path('proxyemployee2/',views.ProxyEmployee2_view),
    ]
