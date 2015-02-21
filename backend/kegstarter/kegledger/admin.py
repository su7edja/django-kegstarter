from django.contrib import admin

from .models import Ledger, LedgerEntry


admin.site.register(Ledger)
admin.site.register(LedgerEntry)
