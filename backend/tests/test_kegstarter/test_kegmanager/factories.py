import decimal
import factory
from factory import fuzzy

from ..test_kegledger import factories as ledger_factory


class TapFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'kegmanager.Tap'

    location = 'Kegerator in the back room. Left handle.'


class BrewerFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'kegmanager.Brewer'

    name = fuzzy.FuzzyText()


class BeerFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'kegmanager.Beer'

    brewer = factory.SubFactory(BrewerFactory)
    name = fuzzy.FuzzyText()
    abv = fuzzy.FuzzyDecimal(low=1, high=100)


class KegFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'kegmanager.Keg'

    beer = factory.SubFactory(BeerFactory)
    gallons = decimal.Decimal('10.11')
    ledger_entry = factory.SubFactory(ledger_factory.LedgerEntryFactoryRegistered)
    purchase_date = None
    tap = factory.SubFactory(TapFactory)
