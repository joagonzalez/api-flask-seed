FROM python:3.6.1-alpine

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

RUN git clone -b master git@github.com:newtech-sm/newcos-infrastructure.git

WORKDIR /newcos-powershell-helper

# if tags needed
# RUN git fetch --tags
# RUN git checkout 0.0.1

ADD ./src/ /newcos-powershell-helper
RUN ls /newcos-powershell-helper

RUN pip install -r /newcos-powershell-helper/requirements.txt

CMD ["python","app.py"]