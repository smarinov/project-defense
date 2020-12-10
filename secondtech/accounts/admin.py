from django.contrib import admin

# Register your models here.
from accounts.models import UserProfile, Comment

admin.site.register(UserProfile)
admin.site.register(Comment)