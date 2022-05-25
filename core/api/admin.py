from django.contrib import admin
from .models import Folders, Items, CustomUser
    
admin.site.register(Folders)
admin.site.register(Items)
admin.site.register(CustomUser)