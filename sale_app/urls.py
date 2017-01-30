from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

urlpatterns=[
    url(r'^$',views.post_list,name='post_list'),
    url(r'^(?P<pk>\d+)/$',views.post_detail,name='post_detail'),
    url(r'^new/$',views.post_new,name='post_new'),
    url(r'^(?P<pk>\d+)/edit/$',views.post_edit,name='post_edit'),
    url(r'^login/$',login,{'template_name':'sale_app/login.html'}),
    url(r'^logout/$',logout,{'template_name':'sale_app/logout.html'}),
    url(r'^register/$',views.register,name='register'),

]
