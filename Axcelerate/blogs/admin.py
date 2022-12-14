from django.contrib import admin

# Register your models here.
from .models import BlogModel, Profile, Job

admin.site.register(BlogModel)
admin.site.register(Job)
admin.site.register(Profile)

