from django.urls import path
from firstApp import views
urlpatterns = [
path('student/',views.Student_view),
path('teacher/',views.Teacher_view),
]
