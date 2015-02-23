from datetime import datetime

from django.core.exceptions import ValidationError
import pytest

from . import factories
from ..test_votingbooth import factories as vote_factories


@pytest.mark.django_db
def test_cannot_vote_in_poll_with_purchased_keg():
    keg = factories.KegFactory(purchase_date=datetime.now())
    poll = vote_factories.PollFactory(kegs_available=[keg])
    with pytest.raises(ValidationError):
        vote_factories.VoteFactory(poll=poll)
