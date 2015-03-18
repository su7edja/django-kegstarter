"""
Voting, polling and ratings for kegs. Community bike-shedding!
"""

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import functional

from kegstarter.kegmanager import models as keg_models


class Poll(models.Model):
    """
    Votes from users on what kegs to buy next. We may need to buy multiple kegs
    at a time, so the polls need to support multiple choices in a vote.
    """
    number_of_votes = models.IntegerField(
        help_text="How many votes are users allowed for this poll (typically "
                  "the number of kegs you plan to purchase at once)")
    creation_date = models.DateTimeField(auto_now_add=True)
    expected_purchase_date = models.DateField(
        blank=True, null=True,
        help_text="When you expect to go and buy they kegs")
    kegs_available = models.ManyToManyField(keg_models.Keg,
        help_text="Kegs in this poll someone is willing to go and pick up.")

    @functional.cached_property
    def closed(self):
        """
        The poll is closed once any of kegs available has been purchased.

        We close a poll when even one keg is purchased, regardless of how many keg votes are allowed per user, to
        avoid creating a voting strategy of waiting for one of several kegs to be purchased so you can stack your votes
        on remaining kegs and reduce the odds of a keg you don't like being bought.
        """

        # This is a semi-sneaky way of saying "Get the first instance"
        return next((True for keg in self.kegs_available.all() if keg.purchase_date is not None), False)

    def __str__(self):
        return '{}'.format(self.creation_date)


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
    keg = models.ForeignKey(keg_models.Keg)
    stars = models.IntegerField(choices=STARS)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, help_text="One user, one rating per keg")

    class Meta:
        unique_together = ('keg', 'user')


class Vote(models.Model):
    """Votes tie to a single keg that's yet to be purchased"""

    keg = models.ForeignKey(keg_models.Keg)
    poll = models.ForeignKey(Poll)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        unique_together = (('keg', 'user'),)

    def clean(self):

        # Validation of when to close voting a poll should be done in the poll (if we check the purchase date on the keg
        # in the vote, users could still vote on closed polls as long as they pick a keg that wasn't purchased).
        if self.poll.closed:
            raise ValidationError('Voting is closed on poll {}.'.format(self.poll.creation_date))

        if self.keg not in self.poll.kegs_available.all():
            raise ValidationError('{} is not in poll {}.'.format(self.keg.__str__(), self.poll.__str__()))

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Vote, self).save(*args, **kwargs)
