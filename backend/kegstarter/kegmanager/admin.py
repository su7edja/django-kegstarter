from django.contrib import admin

from . import models

admin.site.register(models.Keg)
admin.site.register(models.Tap)
