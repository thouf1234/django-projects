from django.urls import path
from firstApp import views
urlpatterns = [
    path('display/',views.display_view),
    ]
