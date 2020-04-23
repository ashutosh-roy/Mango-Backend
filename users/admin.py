from django.contrib import admin
from django.db import models
from .models import users_details,users

admin.site.register(users)
admin.site.register(users_details)