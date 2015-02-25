from datetime import datetime

from django.core.exceptions import ValidationError
import pytest

from ..test_kegmanager import factories as keg_factories
from . import factories as vote_factories


@pytest.mark.django_db
def test_cannot_vote_in_poll_with_purchased_keg():
    keg = keg_factories.KegFactory(purchase_date=datetime.now())
    poll = vote_factories.PollFactory(kegs_available=[keg])
    with pytest.raises(ValidationError):
        vote_factories.VoteFactory(poll=poll)


@pytest.mark.django_db
def test_cannot_vote_on_kegs_not_in_poll():
    keg_in_poll = keg_factories.KegFactory(purchase_date=None)
    keg_not_in_poll = keg_factories.KegFactory(purchase_date=None)
    poll = vote_factories.PollFactory(kegs_available=[keg_in_poll])
    with pytest.raises(ValidationError):
        vote_factories.VoteFactory(poll=poll, keg=keg_not_in_poll)
