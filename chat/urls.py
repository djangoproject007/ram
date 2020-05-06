from django.conf.urls import url
from . import views

app_name = 'chat'

urlpatterns = [

    url(r'^inbox/$', views.inbox, name='inbox'),
    url(r'^inbox/(?P<label>[-_\w.]+)/$', views.chat, name='chat'),
    url(r'^new_chat/$', views.new_chat, name='new_chat'),
    url(r'^new_chat/(?P<username>[-_\w.]+)/$', views.new_chat_create, name='new_chat_create'),

]