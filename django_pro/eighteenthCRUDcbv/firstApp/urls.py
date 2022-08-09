from django.urls import path,re_path
from firstApp import views
urlpatterns = [
    path('retrievelist/',views.book_list_view.as_view(),name='list'),
    re_path('retrievedetail/(?P<pk>\d+)/$',views.book_detail_view.as_view(),name='detail'),# here in the name capturing group we specified '<pk>' and not '<id>' as it will show error because while converting book_detail_view class in to function they may used def book_detail_view(request,pk) and not book_detail_view(request,id)
    path('create/',views.book_create_view.as_view()),
    re_path('update/(?P<pk>\d+)/$',views.book_update_view.as_view()),
    re_path('delete/(?P<pk>\d+)/$',views.book_delete_view.as_view()),
    ]
