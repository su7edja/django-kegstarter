from django.contrib import admin

from .models import Keg, Poll, Rating, Tap, Vote

admin.site.register(Keg)
admin.site.register(Poll)
admin.site.register(Rating)
admin.site.register(Tap)
admin.site.register(Vote)
