from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to="myimage")
    title = models.CharField(max_length=200, null=True, blank=True)
    body = models.CharField(max_length=60, null=True, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')
    unlikes = models.ManyToManyField(User, blank=True, related_name='post_unlikes')

class editprofile(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)

def get_like_url(self):
	return reverse("insta:like")

def get_unlike_url(self):
	return reverse("insta:unlike")
    