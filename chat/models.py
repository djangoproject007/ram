from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Room(models.Model):
    label = models.SlugField(unique=True)
    receiver = models.ForeignKey(User, related_name="receiver")
    sender = models.ForeignKey(User, related_name="sender")

    def get_last_message(self):
        message = Message.objects.filter(room=self).last()
        return message.text if message else ""

    def get_last_message_timestamp(self):
        message = Message.objects.filter(room=self).last()
        return message.timestamp if message else ""

    def __str__(self):
        return self.label


class Message(models.Model):
    room = models.ForeignKey(Room, related_name="messages")
    sender = models.ForeignKey(User)
    text = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now, db_index=True)

    def __str__(self):
        return self.text + " S:" + self.sender.username
