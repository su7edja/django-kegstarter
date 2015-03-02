FROM python:3.4
WORKDIR /code
ADD . /code/
RUN apt-get update && apt-get upgrade -y
RUN pip install -e .\[dev\]
# CMD manage.py runserver 0.0.0.0:8000
