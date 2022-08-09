from django.urls import path
from firstApp import views
urlpatterns = [
    path('tempcookiepageno/', views.temp_cookie_view),
    path('permcookiepageno/', views.perm_cookie_view),
    path('name/', views.name_view),
    path('age/', views.age_view),
    path('gf/', views.gf_view),
    path('result/', views.result_view),
    ]
