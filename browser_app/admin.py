from django.contrib import admin
from .models import Link, RedirectHistory
# Register your models here.
admin.site.register(Link)
admin.site.register(RedirectHistory)