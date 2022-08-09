from django.urls import path
from tempApp import views
urlpatterns = [
    path('wis/', views.tempview),
]
