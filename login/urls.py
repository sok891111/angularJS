from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.login_form, name='form'),
    url(r'^reg_form/$', views.reg_form, name='reg_form'),
    url(r'^reg/$', views.reg, name='reg'),
    url(r'^check_id.ajax$', views.check_id, name='check_id')
    ,url(r'^login$', views.login, name='login')
]

###  Example

# from django.conf.urls import url
# from . import views

# urlpatterns = [
#     url(r'^$', views.IndexView.as_view(), name='index'),
#     url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
#     url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]