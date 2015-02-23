import decimal

import factory


class BrewerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'kegmanager.Brewer'

    name = 'Stone'


class BeerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'kegmanager.Beer'

    brewer = factory.SubFactory(BrewerFactory)
    name = 'IPA'
    abv = decimal.Decimal('8.00')


class TapFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'kegmanager.Tap'

    location = 'Kegerator in the back room. Left handle.'


class KegFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'kegmanager.Keg'

    beer = factory.SubFactory(BeerFactory)
    gallons = decimal.Decimal('10.11')
    price = decimal.Decimal('29.50')
    purchase_date = None
    tap = factory.SubFactory(TapFactory)
    vendor_name = 'Stone Brewing'
