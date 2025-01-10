from django.contrib import admin
from .models import User, Album, Review

# Register your models here.
admin.site.register(Album)
admin.site.register(Review)