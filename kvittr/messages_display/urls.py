from django.conf.urls import patterns, url
from messages_display import views

urlpatterns = patterns('',
	url(r'^$', views.messages, name='messages'),
	url(r'^(\d+)/add_likes$', views.add_likes, name='add_likes'),
	url(r'^(\d+)/$', views.detailed_message, name='detailed_message'),
)