FROM apache/nifi:latest
LABEL maintainer="Nick Green <nicholasjgreen@gmail.com>"

USER root

RUN apt-get update \
        && apt-get install -y python3

COPY ./scripts/*.* ./

RUN apt-get update \
        && apt-get install -y python3 python3-pip \
        && pip3 install -r requirements.txt --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org
