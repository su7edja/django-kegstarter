FROM python:3.4
RUN apt-get update && apt-get install -y npm nodejs-legacy
RUN pip install pip-accel
RUN npm config set cache /code/.cache/.npm
ENV PIP_DOWNLOAD_CACHE=/code/.cache/pip-cache
ENV PIP_ACCEL_CACHE=/code/.cache/pip-accel-cache
ENV PATH=node_modules/.bin:$PATH

WORKDIR /code
ADD . /code/
RUN pip-accel install -e .\[dev\]
RUN npm install
