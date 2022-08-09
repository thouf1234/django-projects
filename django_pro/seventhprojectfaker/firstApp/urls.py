from firstApp import views
from django.urls import path
urlpatterns = [
path('home/',views.indexview),
path('chejob/',views.chennaiview),
path('hydjob/',views.hyderabadview),
path('deljob/',views.delhiview),
]
