from django.contrib import admin
from users.models import ProfileImage, ComplaintLodge
# Register your models here.

@admin.register(ProfileImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'image', 'date']


@admin.register(ComplaintLodge)
class ComplaintLodgeAdmin(admin.ModelAdmin):
    list_display = ['id','category', 'subcategory', 'state', 'Type', 'Desc', 'Doc']

