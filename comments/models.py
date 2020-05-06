from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.comment