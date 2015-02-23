import factory

from ..kegmanager.manager_factories import KegFactory
from ..django_factories import UserFactory


class PollFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'votingbooth.Poll'

    number_of_votes = 1

    @factory.post_generation
    def kegs_available(self, create, extracted, **kwargs):
        if extracted:
            for keg in extracted:
                self.kegs_available.add(keg)


class VoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'votingbooth.Vote'

    keg = factory.SubFactory(KegFactory)
    poll = factory.SubFactory(PollFactory)
    user = factory.SubFactory(UserFactory)
