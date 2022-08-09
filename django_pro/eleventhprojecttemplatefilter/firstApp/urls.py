from django.urls import path
from firstApp import views
urlpatterns = [
    path('upper/', views.upper_view),
    path('lower/', views.lower_view),
    path('title/', views.title_view),
    path('datefilterarg/', views.date_filter_argument_view),
    path('addsufix/', views.add_sufix_view),
    path('timesince/', views.timesince_view),
    path('custfilterslice/', views.cust_filter_slice),
    ]
