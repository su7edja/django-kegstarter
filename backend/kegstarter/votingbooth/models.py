"""
Voting, polling and ratings for kegs. Community bike-shedding!
"""

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

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

    def closed(self):
        """The poll is closed once any of kegs available has been purchased"""

        # This is a semi-sneaky way of saying "Get the first instance"
        return next((True for keg in self.kegs_available
                    if keg.purchase_date is not None), False)

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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, unique=True,
                             help_text="One user, one rating per keg")


class Vote(models.Model):
    """Votes tie to a single keg that's yet to be purchased"""

    keg = models.ForeignKey(keg_models.Keg)
    poll = models.ForeignKey(Poll)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        unique_together = (('keg', 'user'),)

    def clean_keg(self):
        if self.keg.purchase_date is not None:
            raise ValidationError('Keg "{}" has been purchased.'.format(self.keg))

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Vote, self).save(*args, **kwargs)
