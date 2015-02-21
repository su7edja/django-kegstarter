"""
Some assumptions to keep things simple:
1. You only disconnect kegs to take them back to a vendor, so the tap they're on is sufficient location info.
2. Empty kegs will either be refilled or will be returned and the deposit put back into the keg fund, so you don't
   need to keep track of deposits.
3. Beer is always good; it doesn't _really_ matter what we stock. We should use a very basic voting system.
"""
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Tap(models.Model):
    """
    A spout from which you can get a boozy beverage.
    """
    location = models.CharField(max_length=600)

    def __str__(self):
        return self.location


class Keg(models.Model):
    """
    The liquid in the keg, not the container. The container is merely an earthly manifestation of your deposit. The
    beer in the keg is the thing you are talking about when you say, "keg".

    Many beers change from batch to batch, which makes kegs unique by purchase.
    """
    beverage_name = models.CharField(max_length=200)
    # django-measurements doesn't support Django 1.7, or we'd use that to make a MeasurementField. We force a single
    # unit of measurement to make it easier to write a migration when django-measurements gets updated.
    gallons = models.DecimalField(max_digits=4, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    purchase_date = models.DateField(blank=True, null=True)  # Kegs in active polls won't have been purchased yet.
    ratings = models.ManyToManyField(User, through='Rating')
    tap = models.ForeignKey(Tap)
    vendor_name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {} gallons of {}'.format(self.purchase_date, self.gallons, self.beverage_name)


class Poll(models.Model):
    """
    Votes from users on what kegs to buy next. We may need to buy multiple kegs at a time, so the polls need to support
    multiple choices in a vote.
    """
    number_of_allowed_choices = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
    kegs = models.ManyToManyField(Keg)
    votes = models.ManyToManyField(User, through='Vote')

    def __str__(self):
        return '{}: {}'.format(self.creation_date)


class Rating(models.Model):
    """
    User ratings of kegs that have been purchased.
    """
    STARS = [
        (1, 'One Star'),
        (2, 'Two Stars'),
        (3, 'Three Stars'),
        (4, 'Four Stars'),
        (5, 'Five Stars'),
    ]
    keg = models.ForeignKey(Keg)
    stars = models.IntegerField(choices=STARS)
    user = models.ForeignKey(User, unique=True)  # It's not sensical for one user to give two ratings of the same keg.


class Vote(models.Model):
    kegs = models.ManyToManyField(Keg)
    poll = models.ForeignKey(Poll)
    user = models.ForeignKey(User, unique=True)  # We don't want a user to vote twice in the same poll.

    def clean(self):
        purchased_kegs = [k for k in self.poll.kegs.all() if k.purchase_date is not None]
        if purchased_kegs:
            raise ValidationError('You can no longer vote in this poll. One of the kegs has been purchased.')

    def save(self, *args, **kwargs):
        self.clean()
        super(Vote, self).save(*args, **kwargs)
