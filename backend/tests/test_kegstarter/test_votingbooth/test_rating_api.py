from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
import pytest

from .. import django_factories
from . import factories
from kegstarter.votingbooth.models import Rating


@pytest.mark.django_db
def test_cannot_edit_rating_made_by_other_user():
    user = django_factories.UserFactory()
    rating = factories.RatingFactory()
    client = APIClient()
    client.force_authenticate(user)
    data = {"stars": 3, "keg": rating.keg.id, "user": rating.user.id}
    response = client.put(reverse('rating-detail', kwargs={'pk': rating.id}), data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_owner_can_modify_own_keg_rating():
    user = django_factories.UserFactory()
    rating = factories.RatingFactory(user=user)
    client = APIClient()
    client.force_authenticate(user)
    data = {"stars": 3, "keg": rating.keg.id, "user": user.id}
    response = client.put(reverse('rating-detail', kwargs={'pk': rating.id}), data=data, format='json')
    assert Rating.objects.get(id=rating.id).stars == 3
    assert response.status_code == status.HTTP_200_OK
