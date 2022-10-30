from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Link(models.Model):
    full_link = models.URLField()
    short_link = models.CharField(max_length=6, unique=True)
    last_enter_date = models.DateTimeField()
    unique_users_counter = models.IntegerField(default = 0)
    user_ip = models.GenericIPAddressField() #only if no real user
    is_delete = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE,related_name="link") #can be fake user if 'user_ip'

    def __str__(self):
        return self.short_link



