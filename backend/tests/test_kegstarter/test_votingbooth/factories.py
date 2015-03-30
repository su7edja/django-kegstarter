import factory

from ..django_factories import UserFactory

from ..test_kegmanager.factories import KegFactory


class PollFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'votingbooth.Poll'

    number_of_votes = 1

    @factory.post_generation
    def kegs_available(self, create, extracted, **kwargs):
        if extracted:
            self.kegs_available.add(*extracted)


class RatingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'votingbooth.Rating'

    keg = factory.SubFactory(KegFactory)
    stars = 1
    user = factory.SubFactory(UserFactory)


class VoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'votingbooth.Vote'

    keg = factory.SubFactory(KegFactory)
    poll = factory.SubFactory(PollFactory)
    user = factory.SubFactory(UserFactory)
