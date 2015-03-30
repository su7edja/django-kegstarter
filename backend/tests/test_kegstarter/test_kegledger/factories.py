from datetime import datetime
import decimal

import factory

from ..django_factories import UserFactory


class LedgerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'kegledger.Ledger'

    name = 'A Testy Ledger'
    user = factory.SubFactory(UserFactory)


class LedgerEntryFactoryGuest(factory.django.DjangoModelFactory):
    class Meta:
        model = 'kegledger.LedgerEntry'

    amount = decimal.Decimal('12.05')
    time = datetime.now()
    ledger = factory.SubFactory(LedgerFactory)
    notes = 'Those dollar bills were mighty crisp.'
    user = None
    guest_name = factory.Sequence(lambda n: 'Guest{}'.format(n))


class LedgerEntryFactoryRegistered(factory.django.DjangoModelFactory):
    class Meta:
        model = 'kegledger.LedgerEntry'

    amount = decimal.Decimal('12.05')
    time = datetime.now()
    ledger = factory.SubFactory(LedgerFactory)
    notes = 'Those dollar bills were mighty crisp.'
    user = factory.SubFactory(UserFactory)
    guest_name = ''
