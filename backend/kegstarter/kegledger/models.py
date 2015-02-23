from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Ledger(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User)

    @property
    def total(self):
        return LedgerEntry.objects.filter(ledger=self).aggregate(models.Sum('amount'))['amount__sum']

    def __str__(self):
        return '{}: ${}'.format(self.name, self.total)


class LedgerEntry(models.Model):

    amount = models.DecimalField(max_digits=8, decimal_places=2)
    # Don't auto_add_now; you shouldn't have to be logged in to accept a contribution.
    time = models.DateTimeField()
    ledger = models.ForeignKey(Ledger)
    notes = models.CharField(max_length=600, blank=True)
    # No barriers to beer; you don't need an account to contribute to the keg fund.
    user = models.ForeignKey(User, blank=True, null=True)
    # Without an account we need your name so we can find your contributions later.
    guest_name = models.CharField(max_length=200, blank=True)

    def clean(self):
        if self.user is None and not self.guest_name:
            raise ValidationError('Either select a registered user or enter a guest name.')
        if self.guest_name and self.user:
            raise ValidationError('Only enter a guest name for users who are not registered.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super(LedgerEntry, self).save(*args, **kwargs)

    def __str__(self):
        name = self.user.username if self.user else self.guest_name
        return '{}: {} ${}'.format(self.time.date(), name, self.amount)

    class Meta:
        verbose_name = 'Ledger Entry'
        verbose_name_plural = 'Ledger Entries'
