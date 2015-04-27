from django.conf.urls import patterns, url

from messages_display import views

urlpatterns = patterns('',
	url(r'^$', views.messages, name='messages'),
)