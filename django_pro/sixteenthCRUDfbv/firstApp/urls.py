from firstApp import views
from django.urls import path, re_path
urlpatterns = [
path('retrieve/',views.retrieve_view),
path('create/',views.create_view),
#path('delete/<int:id>/',views.delete_view), # both the url in 6th line and 7th line works fine and valid, sor use any of them
re_path('delete/(?P<id>\d+)/$',views.delete_view),
re_path('update/(?P<id>\d+)/$',views.update_view),
]
