import pytest

from django.db import IntegrityError

from ..test_kegmanager import factories as keg_factories
from . import factories as vote_factories


@pytest.mark.django_db
def test_no_duplicate_keg_user_tuple():
    user = vote_factories.UserFactory()
    keg = keg_factories.KegFactory()
    vote_factories.RatingFactory(keg=keg, user=user)
    with pytest.raises(IntegrityError):
        vote_factories.RatingFactory(keg=keg, user=user, stars=5)
