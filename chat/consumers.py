from django.contrib.auth.models import User
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
from .models import Room
import json

"""
@channel_session, provides message.chanel_session
"""

# Connected to websocket.connect
@channel_session_user_from_http
def ws_connect(message):
    path = message.content['path']
    room_label = path.replace('/chat/inbox/', '').replace('/', '')
    room = Room.objects.get(label=room_label)

    Group('chat-' + room_label).add(message.reply_channel)
    message.channel_session['room'] = room.label


# Connected to websocket.receive
@channel_session_user
def ws_receive(message):
    path = message.content['path']
    room_label = path.replace('/chat/inbox/', '').replace('/', '')
    room = Room.objects.get(label=room_label)
    data = json.loads(message['text'])
    text = data['message']

    sender = User.objects.get(username=data['user'])
    m = room.messages.create(sender=sender, text=text)

    try:
        avatar_url = sender.userprofiledata.avatar.url
    except:
        avatar_url = '/static/images/profile_placeholder.jpg'

    context = {
        'text': m.text,
        'user': sender.username,
        'avatar': avatar_url,
    }
    Group('chat-'+ room_label).send({'text': json.dumps(context) })


# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message):
    label = message.channel_session['room']
    Group('chat-'+label).discard(message.reply_channel)
