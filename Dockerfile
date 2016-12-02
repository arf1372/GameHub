FROM python:latest
MAINTAINER Kian Ahrabian <kahrabian@yahoo.com>

ENV LAST_UPDATED 2016-12-01

RUN apt-get update -qq && apt-get upgrade -qqy
RUN apt-get install -qqy libmemcached-dev

ADD ./configs/pip/requirements.txt /root/
RUN pip install -r /root/requirements.txt

ADD . /home/admin/dooz
WORKDIR /home/admin/dooz

CMD ["./docker-entrypoint.sh"]
