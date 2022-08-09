from django.urls import path, re_path
from blog import views
urlpatterns = [
    re_path('home/(?:(?P<tag_slug>[-\w]+)/)?$',views.post_list_view,name='post_list_url'),#use PostListView.as_view() to implement class based view
    re_path('detail/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',views.post_detail_view,name='post_detail'),#here $ dolar means after that you should not take anything(end character) and [-\w]+ means atleast one '-' iphen character and alphabet character )
    re_path('mail/(?P<id>\d+)/$',views.mail_Send_view,name='send_mail')
    ]
