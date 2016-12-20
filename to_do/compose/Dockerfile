################################################################
# Dockerfile to deploy a nginx caching 
# Based on Ubuntu 14.04
################################################################

# Setting the base image to Ubuntu 14.04
FROM ubuntu:14.04

MAINTAINER Alex Vaque

RUN apt-get update && \
    apt-get -y install python python-pip python-dev

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

