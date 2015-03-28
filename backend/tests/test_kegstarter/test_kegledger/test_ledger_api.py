from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
import pytest

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


# The permissions system says you can edit a ledger entry if you own it (i.e. are in the user field on that model
# instance). It may make more sense to say you can edit an entry if and only if you own the ledger itself.
@pytest.mark.xfail
@pytest.mark.django_db
def test_cannot_edit_ledger_entry_unless_you_own_ledger():
    user = django_factories.UserFactory()
    ledger = factories.LedgerFactory()
    ledger_entry = factories.LedgerEntryFactoryRegistered(ledger=ledger, user=user_b)
    client = APIClient()
    client.force_authenticate(user=user)
    data = {"amount": 10, "time": "2015-03-28T20:43:21Z", "ledger": ledger.id}
    response = client.put(reverse('ledger-entry-detail', kwargs={'pk': ledger_entry.id}), data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN
