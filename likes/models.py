from django.db import models
from posts.models import Post
from django.contrib.auth.models import User


class Like(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)

    class Meta:
        unique_together = ("post", "user")
