from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^retrieveMessage/$', views.retrieveMessageView.as_view(), name='message-list'),
	url(r'^createMessage/$', views.CreateMessageView.as_view(), name='message-create'),
] 