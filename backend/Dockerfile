FROM python:3.4
RUN apt-get update && apt-get upgrade -y

ADD setup.py /tmp/python-setup/setup.py
WORKDIR /tmp/python-setup
RUN python setup.py list_deps -e dev | tail -n1 | xargs pip install

ADD . /opt/kegstarter-django
WORKDIR /opt/kegstarter-django
RUN pip install -e .[dev]
