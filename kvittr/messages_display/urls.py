from django.conf.urls import patterns, url
from messages_display import views

urlpatterns = patterns('',
	url(r'^$', views.messages, name='messages'),
	url(r'^(\d+)/increase_likes$', views.like_button, 
		name='like_button'),
)