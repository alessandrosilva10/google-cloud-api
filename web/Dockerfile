# pull official base image
FROM python:3.8.1-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y libpq-dev && \
    apt-get install -y gcc && \
    apt-get install -y apt-utils
   
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/