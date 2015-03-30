from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
import pytest

from .. import django_factories
from . import factories


@pytest.mark.django_db
def test_cannot_edit_rating_made_by_other_user():
    user = django_factories.UserFactory()
    rating = factories.RatingFactory()
    client = APIClient()
    client.force_authenticate(user)
    data = {"stars": 3, "keg": rating.keg.id, "user": rating.user.id}
    response = client.put(reverse('rating-detail', kwargs={'pk': rating.id}), data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN
