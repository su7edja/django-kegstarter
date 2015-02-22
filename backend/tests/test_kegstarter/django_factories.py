from django.contrib.auth.models import User

import factory


class UserFactory(factory.DjangoModelFactory):
    """
    Credit to Martin Brochhaus for the _prepare method: https://gist.github.com/mbrochh/2433411
    """
    FACTORY_FOR = User

    username = factory.Sequence(lambda n: 'User{}'.format(n))
    email = factory.Sequence(lambda n: 'user{}@example.com'.format(n))

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = 'test123'
        if 'password' in kwargs:
            password = kwargs.pop('password')
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        user.set_password(password)
        if create:
            user.save()
        return user
