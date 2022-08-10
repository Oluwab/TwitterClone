from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Post(models.Model):
    class Meta(object):
        db_table = 'post'
    name = models.CharField(
        'name', blank=False, null=True, max_length=14, db_index=True, default='anonymous',
    )
    body = models.CharField(
        'body', blank=True, null=True, max_length=140, db_index=True,
    )
    created_at = models.DateTimeField(
        'created DateTime', blank=True, auto_now_add=True,
    )
    likes = models.PositiveIntegerField(
        'like', default=0, blank=True, db_index=True,
    )
    image = CloudinaryField(
        'image', blank=True, db_index=True,
    )
   