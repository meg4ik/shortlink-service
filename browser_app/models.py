from email.policy import default
from enum import unique
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Link(models.Model):
    full_link = models.URLField()
    short_link = models.CharField(max_length=6, unique=True)
    last_enter_date = models.DateTimeField()
    unique_users_counter = models.IntegerField(default = 0)
    user_ip = models.GenericIPAddressField(unique=True) #only if no real user
    is_delete = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE,related_name="link")