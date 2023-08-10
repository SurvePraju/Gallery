from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(UploadImage)
class adminregister(admin.ModelAdmin):
    list_display = ["user", "image_name", "category", "image", "upload_date"]


@admin.register(UserInformation)
class adminregister(admin.ModelAdmin):
    list_display = ["user", "contact", "profile_image"]
