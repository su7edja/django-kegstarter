import factory

from ..django_factories import UserFactory


class PollFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'votingbooth.Poll'

    number_of_votes = 1

    @factory.post_generation
    def kegs_available(self, create, extracted, **kwargs):
        if extracted:
            self.kegs_available.add(*extracted)


class VoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'votingbooth.Vote'

    poll = factory.SubFactory(PollFactory)
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def kegs(self, create, extracted, **kwargs):
        if extracted:
            for keg in extracted:
                self.kegs.add(keg)
