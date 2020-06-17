FROM python:3.6.1-alpine

LABEL maintainer="Joaquin Gonzalez <joagonzalez@gmail.com>"

RUN pip install --upgrade pip

ARG SSH_KEY
ENV SSH_KEY=$SSH_KEY

RUN apk update

RUN apk add openssh-client  \
        && apk add git \
        && apk add iputils

# Make ssh dir
RUN mkdir /root/.ssh/
# Create id_rsa from string arg, and set permissions
RUN echo "$SSH_KEY" > /root/.ssh/id_rsa
RUN chmod 400 /root/.ssh/id_rsa
# Create known_hosts
RUN touch /root/.ssh/known_hosts
# Add git providers to known_hosts
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

RUN git clone -b master git@github.com:joagonzalez/api-flask-seed.git
RUN git checkout refactor
WORKDIR /api-flask-seed

# if tags needed
# RUN git fetch --tags
# RUN git checkout 0.0.1

ADD ./src/ /api-flask-seed
RUN ls /api-flask-seed

RUN pip install -r /api-flask-seed/requirements.txt
RUN cd /api-flask-seed

CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:5000", "-w 4"]
