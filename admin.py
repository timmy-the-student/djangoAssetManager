from django.contrib import admin
from .models import asset
from .models import default

# Register your models here.
admin.site.register(default)
admin.site.register(asset)