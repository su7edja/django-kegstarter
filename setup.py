from setuptools import setup, find_packages


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
      scripts=['backend/kegstarter/manage.py'],
      package_dir={'': 'backend'},
      packages=find_packages(where='backend', exclude=('tests*',)),
      include_package_data=True,
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
