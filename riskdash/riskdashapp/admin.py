from django.contrib import admin

from .models import Risk,Risk_type,Controls

admin.site.register(Risk)
admin.site.register(Risk_type)
admin.site.register(Controls)
