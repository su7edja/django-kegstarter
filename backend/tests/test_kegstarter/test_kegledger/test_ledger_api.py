import pytest
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from rest_framework.test import force_authenticate

from .factories import LedgerFactory, LedgerEntryFactoryRegistered
from ..django_factories import UserFactory
from kegstarter.kegledger.api import LedgerViewSet, LedgerEntryViewSet
from kegstarter.kegledger.models import LedgerEntry


class KegLedgerAPITest(APITestCase):
    def test_ledger_list(self):
        LedgerFactory()
        LedgerFactory()
        factory = APIRequestFactory()
        request = factory.get('kegstarter/kegledger/api/ledgers')
        view = LedgerViewSet.as_view({'get': 'list'})
        response = view(request)
        response.render()
        self.assertEqual(len(response.data), 2)

    def test_ledger_detail(self):
        LedgerFactory()
        LedgerFactory(name='Ledger 2', owner__username='UserName')
        factory = APIRequestFactory()
        request = factory.get('kegstarter/kegledger/api/ledgers/2')
        view = LedgerViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk='2')
        response.render()
        self.assertEqual(response.data['name'], 'Ledger 2')

    def test_admin_can_create_ledger(self):
        pass

    def test_admin_can_delete_ledger(self):
        pass

    def test_non_admin_cannot_create_ledger(self):
        pass

    def test_non_admin_cannot_delete_ledger(self):
        pass

    def test_ledger_owner_can_add_ledger_entry(self):
        ledger = LedgerFactory(name='Ledger', owner__username='UserName')
        LedgerEntryFactoryRegistered(ledger=ledger)
        entry = LedgerEntryFactoryRegistered(amount=5, ledger=ledger)
        factory = APIRequestFactory()

        print "before", LedgerEntry.objects.count()
        client = APIClient()
        user = UserFactory()
        client.login(username=user.username, password=user.password)
        response = client.delete(reverse('ledgerentry-detail', args=str(entry.pk)))
        print LedgerEntry.objects.count()
        print response.data
        print response.status_code
        # self.assertEqual(resp2.data['name'], 'Ledger')

    def test_ledger_owner_can_delete_ledger_entry(self):
        pass

    def test_non_ledger_owner_cannot_add_ledger_entry(self):
        pass

    def test_non_ledger_owner_cannot_delete_ledger_entry(self):
        pass

    def test_anonymous_cannot_view_ledger(self):
        # user must be logged in to be able to view. This is currently not implemented. Anyone can view.
        pass

    def test_ledger_owner_add_ledger_entry(self):
        pass

    def test_non_ledger_owner_cannot_edit_ledger_entry(self):
        pass

    def test_anonymous_cannot_view_ledger_entry(self):
        # user must be logged in to be able to view. This is currently not implemented. Anyone can view.
        pass
