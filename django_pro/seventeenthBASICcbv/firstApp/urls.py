from django.urls import path
from firstApp import views
urlpatterns = [
    path('cbv/',views.HelloworldView.as_view()),
    path('cbvtemplate/',views.HelloworldTemplateView.as_view()),
    path('cbvtemplatecontext/',views.HelloworldTemplateContext.as_view()),
    ]
