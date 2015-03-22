import pytest
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIRequestFactory

from .factories import LedgerFactory, LedgerEntryFactoryRegistered
from ..django_factories import UserFactory
from kegstarter.kegledger.api import LedgerViewSet, LedgerEntryViewSet


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

    def test_owner_can_edit_ledger(self):
        ledger = LedgerFactory(name='Ledger', owner__username='UserName')
        LedgerEntryFactoryRegistered(ledger=ledger)
        LedgerEntryFactoryRegistered(amount=5, ledger=ledger)
        factory = APIRequestFactory()
        # request = factory.get('kegstarter/kegledger/api/ledgers/1')
        # view = LedgerViewSet.as_view({'get': 'retrieve'})
        # response = view(request, pk='1')
        # response.render()
        #
        # r = factory.delete('kegstarter/kegledger/api/entries/2') #r.user is Anonymous, so it is expected that we cannot delete
        # owner = User.objects.get(username='UserName')
        # r.user = owner
        v = LedgerEntryViewSet.as_view({'get': 'retrieve', 'post': 'destroy'})
        # resp = v(r, pk='2')
        # resp.render()

        from kegstarter.kegledger.models import LedgerEntry
        user = LedgerEntry.objects.get(pk=2).user
        r2 = factory.delete('kegstarter/kegledger/api/entries/2')
        r2.user = user
        resp2 = v(r2, pk='2')
        resp2.render()
        print resp2.data
        self.assertEqual(resp2.data['name'], 'Ledger')

    def test_non_owner_cannot_edit_ledger(self):
        # user must be logged in to be able to view. This is currently not implemented. Anyone can view.
        pass

    def test_anonymous_cannot_view_ledger(self):
        pass

    def test_owner_add_ledger_entry(self):
        pass

    def test_non_owner_cannot_edit_ledger_entry(self):
        # user must be logged in to be able to view. This is currently not implemented. Anyone can view.
        pass

    def test_anonymous_cannot_view_ledger_entry(self):
        pass
