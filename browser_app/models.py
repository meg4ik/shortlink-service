from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Link(models.Model):
    full_link = models.URLField()
    short_link = models.CharField(max_length=6, unique=True)
    user_ip = models.GenericIPAddressField() #only if no real user
    is_delete = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE,related_name="link") #can be fake user if 'user_ip'


class RedirectHistory(models.Model):
    enter_user_ip = models.GenericIPAddressField()
    enter_date = models.DateTimeField()
    link = models.ForeignKey(Link, on_delete = models.CASCADE,related_name="link_history")

    def __str__(self):
            return "{} - {}".format(self.enter_date, self.enter_user_ip)