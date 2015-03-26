from setuptools import setup, find_packages, Command
from distutils import log


class ListDeps(Command):
    user_options = [
        ('extras=', 'e', 'Extra requirements to list'),
    ]

    def initialize_options(self):
        self.extras = None

    def finalize_options(self):
        extras = ()
        if self.extras is not None:
            extras = self.extras.lstrip('=').split(',')
        requirements = self.distribution.install_requires[:]
        requirements.extend(req
            for key in extras
            for req in self.distribution.extras_require[key]
        )
        self.announce(' '.join(requirements), log.INFO)

    def run(self):
        return


requirements = [
    'Django==1.7.4',
    'django-configurations==0.8',
    'dj-database-url==0.3.0',
    'djangorestframework==3.0.5',
    'psycopg2==2.6',
]


testing_requirements = [
    'flake8==2.3.0',
    'pytest-cache==1.0',
    'pytest-cov==1.8.1',
    'pytest-django==2.7.0',
    'factory-boy==2.4.1',
    'six==1.5.2',  # This is not being installed for some reason?
    'Sphinx==1.2.2',
    'sphinx_rtd_theme==0.1.6',
    'tox==1.8.1',
]

development_requirements = [
    'ipdb',
    'ipython',
]

production_requirements = [
    'gunicorn==19.1.1',
]


setup(name='django-kegstarter',
      version='0.1.0',
      description='Kegerator management for offices',
      author='Paul Collins',
      author_email='paul.collins.iii@gmail.com',
      license='All Rights Reserved',
      install_requires=requirements,
      extras_require={
          'dev': development_requirements + testing_requirements,
          'prod': production_requirements,
          'testing': testing_requirements,
      },
      scripts=['kegstarter/manage.py'],
      packages=find_packages(where='.', exclude=('tests*',)),
      include_package_data=True,
      cmdclass={'list_deps': ListDeps},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Programming Language :: Python :: 3.4',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Internet :: WWW/HTTP :: WSGI',
      ],
      )
