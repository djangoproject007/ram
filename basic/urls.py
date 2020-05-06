from django.conf.urls import url
from . import views

app_name = 'basic'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^signup_success/$', views.signup_success, name='signup_success'),
    url(r'about/$', views.see_about, name='about'),
    url(r'privacy/$', views.see_privacy, name='privacy'),
    url(r'terms/$', views.see_terms, name='terms'),
    url(r'^about/overview/circulars', views.circularredirect, name='circularredirect'),
    url(r'^explore/$', views.explore, name='explore'),
    url(r'^circulars/$', views.circulars, name='circulars'),
    url(r'^directory/$', views.directory, name='directory'),

]
