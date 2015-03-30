from django.contrib import admin

from . import models

admin.site.register(models.Beer)
admin.site.register(models.Brewer)
admin.site.register(models.Keg)
admin.site.register(models.Tap)
