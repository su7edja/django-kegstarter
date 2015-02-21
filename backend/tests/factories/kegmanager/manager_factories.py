import decimal

import factory

from ..django_factories import UserFactory


class TapFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'kegmanager.Tap'

    location = 'Kegerator in the back room. Left handle.'


class KegFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'kegmanager.Keg'

    beverage_name = 'Stone IPA'
    gallons = decimal.Decimal('10.11')
    price = decimal.Decimal('29.50')
    purchase_date = None
    tap = factory.SubFactory(TapFactory)
    vendor_name = 'Stone Brewing'


class PollFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'kegmanager.Poll'

    number_of_allowed_choices = 1

    @factory.post_generation
    def kegs(self, create, extracted, **kwargs):
        if extracted:
            for keg in extracted:
                self.kegs.add(keg)


class VoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'kegmanager.Vote'

    poll = factory.SubFactory(PollFactory)
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def kegs(self, create, extracted, **kwargs):
        if extracted:
            for keg in extracted:
                self.kegs.add(keg)
