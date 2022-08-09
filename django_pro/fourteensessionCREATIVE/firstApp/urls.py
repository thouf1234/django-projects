from django.urls import path
from firstApp import views
urlpatterns = [
    path('form/', views.form_view),
    path('result/', views.result_view),
    path('del/', views.del_view),
    ]
