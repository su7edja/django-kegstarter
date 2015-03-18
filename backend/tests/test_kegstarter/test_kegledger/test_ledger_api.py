import pytest
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase, APIRequestFactory

from .factories import LedgerFactory, LedgerEntryFactoryRegistered
from ..django_factories import UserFactory
from kegstarter.kegledger.api import LedgerViewSet


class KegLedgerAPITest(APITestCase):
    def test_owner_can_edit_ledger(self):
        owner = UserFactory(username='Owner')
        ledger = LedgerFactory(owner=owner)
        factory = APIRequestFactory()
        request = factory.post('kegstarter/kegledger/api/ledgers', {'name': 'Test Ledger'})
        view = LedgerViewSet.as_view({'get': 'list'}) #'detail'
        response = view(request)
        response.render()
        print response


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
