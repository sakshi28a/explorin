from django.contrib import admin
from .models import Image, editprofile

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo', 'body', 'id']

@admin.register(editprofile)
class editprofileAdmin(admin.ModelAdmin):
    list_display = ['name']
