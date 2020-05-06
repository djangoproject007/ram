from django.db import models
from imagekit.models import ProcessedImageField
#other apps
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    image = ProcessedImageField(upload_to='posts',format='JPEG',options={'quality': 100}, null=True, blank=True)
    title = models.CharField(max_length=60)
    content = models.TextField(max_length=1024)
    time_created = models.DateTimeField(auto_now=True, auto_now_add=False)
    time_updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_number_of_likes(self):
        return self.like_set.count()

    def get_number_of_comments(self):
        return self.comment_set.count()

    def __str__(self):
        return self.title