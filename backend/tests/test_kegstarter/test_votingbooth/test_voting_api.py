import pytest
from datetime import datetime

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from kegstarter.votingbooth.models import Vote, Poll
from .. import django_factories
from ..test_kegmanager import factories as keg_factories
from . import factories as vote_factories


@pytest.mark.django_db
def test_cannot_edit_votes_made_by_other_user():
    user = django_factories.UserFactory()
    keg = keg_factories.KegFactory()
    poll = vote_factories.PollFactory(kegs_available=[keg])
    vote = vote_factories.VoteFactory(poll=poll, keg=keg)
    client = APIClient()
    client.force_authenticate(user=user)
    data = {"keg": vote.keg.id, "poll": vote.poll.id, "user": vote.user.id}
    response = client.put(reverse('vote-detail', kwargs={'pk': vote.id}), data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_can_edit_own_vote_in_open_poll():
    user = django_factories.UserFactory()
    keg1 = keg_factories.KegFactory()
    keg2 = keg_factories.KegFactory()
    poll = vote_factories.PollFactory(kegs_available=[keg1, keg2])
    vote = vote_factories.VoteFactory(poll=poll, keg=keg1, user=user)
    client = APIClient()
    client.force_authenticate(user=user)
    old_voted_keg = vote.keg
    data = {"keg": keg2.id, "poll": poll.id, "user": user.id}
    response = client.put(reverse('vote-detail', kwargs={'pk': vote.id}), data, format='json')
    new_voted_keg = Vote.objects.get(id=vote.id).keg
    assert old_voted_keg != new_voted_keg
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_cannot_edit_votes_in_closed_polls():
    user = django_factories.UserFactory()
    keg = keg_factories.KegFactory()
    poll = vote_factories.PollFactory(kegs_available=[keg])
    vote = vote_factories.VoteFactory(user=user, poll=poll, keg=keg)
    keg.purchase_date = datetime.now()
    keg.save()
    client = APIClient()
    client.force_authenticate(user=user)
    data = {"keg": keg.id, "poll": poll.id, "user": user.id}
    response = client.put(reverse('vote-detail', kwargs={'pk': vote.id}), data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_cannot_edit_closed_poll():
    user = django_factories.UserFactory(is_staff=True)
    keg = keg_factories.KegFactory(purchase_date=datetime.now())
    poll = vote_factories.PollFactory(kegs_available=[keg])
    client = APIClient()
    client.force_authenticate(user=user)
    data = {"number_of_votes": 4, "kegs_available": [keg.id]}
    response = client.put(reverse('poll-detail', kwargs={'pk': poll.id}), data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_must_be_admin_to_edit_poll():
    user = django_factories.UserFactory()
    keg = keg_factories.KegFactory()
    poll = vote_factories.PollFactory(kegs_available=[keg])
    client = APIClient()
    client.force_authenticate(user=user)
    data = {"number_of_votes": 4, "kegs_available": [keg.id]}
    response = client.put(reverse('poll-detail', kwargs={'pk': poll.id}), data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_admin_can_edit_open_poll():
    user = django_factories.UserFactory(is_staff=True)
    keg = keg_factories.KegFactory()
    poll = vote_factories.PollFactory(kegs_available=[keg])
    client = APIClient()
    client.force_authenticate(user=user)
    data = {"number_of_votes": 4, "kegs_available": [keg.id]}
    response = client.put(reverse('poll-detail', kwargs={'pk': poll.id}), data, format='json')
    assert Poll.objects.get(id=poll.id).number_of_votes == 4
    assert response.status_code == status.HTTP_200_OK
