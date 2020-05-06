#django
from django.db import models
from django.contrib.auth.models import User

#packages
from imagekit.models import ProcessedImageField


class UserProfileData(models.Model):
    class Meta:
        db_table = 'user_profile_data'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name="followers_profile", blank=True)

    following = models.ManyToManyField(User, related_name="following_profile", blank=True)

    status = models.TextField(max_length=100, null=True, blank=True, default="Yeah! I am at HUSKY!")
    avatar = ProcessedImageField(upload_to='profile_pics',format='JPEG',options={ 'quality': 100},null=True,blank=True)
    secondary_email = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.PositiveIntegerField(blank=True, null=True)
    fb = models.CharField(max_length=1000, null=True, blank=True, default="http://facebook.com/")
    instagram = models.CharField(max_length=1000, null=True, blank=True, default="http://instagram.com/")
    github = models.CharField(max_length=1000, null=True, blank=True, default="http://github.com/")
    linkedin = models.CharField(max_length=200, null=True, blank=True, default="http://linkedin.com/")

    def get_number_of_followers(self):
        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    def get_number_of_following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0

    def __str__(self):
        return self.user.username
