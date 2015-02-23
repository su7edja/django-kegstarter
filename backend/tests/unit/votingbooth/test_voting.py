from datetime import datetime

from django.core.exceptions import ValidationError
import pytest

from ...factories.kegmanager.manager_factories import KegFactory
from ...factories.votingbooth.voting_factories import PollFactory, VoteFactory


@pytest.mark.django_db
def test_cannot_vote_in_poll_with_purchased_keg():
    keg = KegFactory(purchase_date=datetime.now())
    poll = PollFactory(kegs_available=[keg])
    with pytest.raises(ValidationError):
        VoteFactory(poll=poll)
