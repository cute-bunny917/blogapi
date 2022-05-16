# posts/admin.py
from django.contrib import admin
from .models import Post

#  view our data in Django’s built-in admin app
admin.site.register(Post)
