from django.contrib import admin

from .models import Image

class ImageAdmin(admin.ModelAdmin):
	fields = ["name","url","stock","prix",]
    
admin.site.register(Image)