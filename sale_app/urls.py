from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

urlpatterns=[
    url(r'^$',views.post_list,name='post_list'),
    url(r'^sale_app/(?P<pk>\d+)/$',views.post_detail,name='post_detail'),
    url(r'^sale_app/new/$',views.post_new,name='post_new'),
    url(r'^sale_app/(?P<pk>\d+)/edit/$',views.post_edit,name='post_edit'),
    url(r'^sale_app/login/$',login,{'template_name':'sale_app/login.html'}),
    url(r'^sale_app/logout/$',logout,{'template_name':'sale_app/logout.html'}),
    url(r'^sale_app/register/$',views.register,name='register'),

]
