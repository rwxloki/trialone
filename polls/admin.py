from django.contrib import admin

from .models import BlogMod, Mymod

admin.site.register(Mymod)

admin.site.register(BlogMod)