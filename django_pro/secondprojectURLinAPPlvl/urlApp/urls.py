from django.urls import path
from urlApp import views
urlpatterns = [
    path('chennai/',views.chennai),
    path('ooty/',views.ooty),
    path('mysore/',views.mysore),
    ]
