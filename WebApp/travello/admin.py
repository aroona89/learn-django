from django.contrib import admin
from travello.models import Destination

# Register your models here.

# @admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'img' , 'desc' , 'price', 'offer')

admin.site.register(Destination, DestinationAdmin)
