from django.urls import path
from firstApp import views
urlpatterns = [
path('home/',views.home_view),
path('form/',views.Djform_view),
path('view/',views.view_view),
]
