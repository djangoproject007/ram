from django.conf.urls import url
from . import views

app_name = 'notifications'

urlpatterns = [

    url(r'^notifications/$', views.notifications, name='notifications'),

]