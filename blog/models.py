from django.db import models
from django.contrib.auth.models import User
import os
from taggit.managers import TaggableManager

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = TaggableManager()
    summary = models.TextField(max_length=200,default='')
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('images', instance)
        return None
    image = models.ImageField(upload_to=image_upload_to, max_length=255)


class Meta:
        ordering = ['-created_on']

def __str__(self):
        return self.title

class SubscribedUsers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField(auto_now=True)

