import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from .. import django_factories
from . import factories


@pytest.mark.django_db
def test_cannot_edit_ledger_owned_by_other_user():
    user = django_factories.UserFactory()
    ledger = factories.LedgerFactory()
    client = APIClient()
    client.force_authenticate(user=user)
    data = {"name": "sodifnoiwnlsdinfoiwenlsdkn", "user": ledger.user.id}
    response = client.put(reverse('ledger-detail', kwargs={'pk': ledger.id}), data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_cannot_edit_ledger_entry_unless_you_own_ledger():
    user = django_factories.UserFactory()
    ledger_owner = django_factories.UserFactory()
    ledger = factories.LedgerFactory(user=ledger_owner)
    ledger_entry = factories.LedgerEntryFactoryRegistered(ledger=ledger, user=user)
    client = APIClient()
    client.force_authenticate(user=user)
    data = {"amount": 10, "time": "2015-03-28T20:43:21Z", "ledger": ledger.id}
    response = client.put(reverse('ledgerentry-detail', kwargs={'pk': ledger_entry.id}), data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_ledger_owner_can_add_entry():
    user = django_factories.UserFactory()
    ledger = factories.LedgerFactory(user=user)
    client = APIClient()
    client.force_authenticate(user=user)
    data = {"amount": 10, "time": "2015-03-28T20:43:21Z", "ledger": ledger.id, "user": user.id}
    response = client.post(reverse('ledgerentry-list'), data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_ledger_owner_can_delete_entry():
    ledger_owner = django_factories.UserFactory()
    ledger = factories.LedgerFactory(user=ledger_owner)
    ledger_entry = factories.LedgerEntryFactoryRegistered(ledger=ledger)
    client = APIClient()
    client.force_authenticate(user=ledger_owner)
    response = client.delete(reverse('ledgerentry-detail', kwargs={'pk': ledger_entry.pk}), format='json')
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_non_ledger_owner_cannot_add_entry():
    user = django_factories.UserFactory()
    ledger = factories.LedgerFactory()
    client = APIClient()
    client.force_authenticate(user=user)
    data = {"amount": 10, "time": "2015-03-28T20:43:21Z", "ledger": ledger.id, "guest_name": "A Guest!"}
    response = client.post(reverse('ledgerentry-list'), data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_anyone_can_view_ledger():
    user = django_factories.UserFactory()
    ledger = factories.LedgerFactory()
    ledger_entry = factories.LedgerEntryFactoryRegistered(ledger=ledger)
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.get(reverse('ledgerentry-detail', kwargs={'pk': ledger_entry.pk}), format='json')
    assert response.status_code == status.HTTP_200_OK
