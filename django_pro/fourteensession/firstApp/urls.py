from django.urls import path
from firstApp import views
urlpatterns = [
    path('pagenosession/', views.pageno_session_view),
    path('name/', views.session_form_name_view),
    path('age/', views.session_form_age_view),
    path('gf/', views.session_form_gf_view),
    path('result/', views.session_form_result_view),
    ]
