from django.contrib import admin
from .models import Category,Image,Location
from .models import Photo

# Register your models here.
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Location)

