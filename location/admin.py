from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Contact)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('username', 'lat', 'lng', 'date')

admin.site.register(Location, LocationAdmin)
