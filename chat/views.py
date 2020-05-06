from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from . models import Room


@login_required
def inbox(request):
    user = request.user
    rooms = Room.objects.filter(Q(receiver=user) | Q(sender=user))
    context = {
        'rooms': rooms
    }
    return render(request, 'chat/inbox.html', context)


@login_required
def chat(request, label):
    room = Room.objects.get(label=label)
    messages = reversed(room.messages.order_by('-timestamp')[:50])

    context = {
        'room': room,
        'messages': messages
    }
    return render(request, 'chat/chat.html', context)


@login_required
def new_chat(request):
    profiles = request.user.userprofiledata.following.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'chat/new_chat.html', context)


@login_required
def new_chat_create(request, username):
    user_to_message = User.objects.get(username=username)
    room_label = request.user.username + '_' + user_to_message.username

    try:
        does_room_exist = Room.objects.get(label=room_label)
    except:
        room = Room(label=room_label, receiver=user_to_message,
                    sender=request.user)
        room.save()

    return redirect('chat:chat', label=room_label)

