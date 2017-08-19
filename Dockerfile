# nginx-gunicorn-flask

FROM python:3.6.2
MAINTAINER Bruno Rocha <rochacbruno@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y nginx supervisor

# Setup flask application
RUN mkdir -p /deploy/app
COPY pt15 /deploy/app
COPY requirements.txt /deploy/app/requirements.txt

# Setup nginx
RUN rm /etc/nginx/sites-enabled/default
COPY pt15/app_nginx.conf /etc/nginx/sites-available/flask.conf
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Setup supervisord
RUN mkdir -p /var/log/supervisor
COPY pt15/app_supervisor.conf /etc/supervisor/conf.d/supervisord.conf

RUN python3.6 -m venv /deploy/app/env
RUN /deploy/app/env/bin/pip3 install -r /deploy/app/requirements.txt

# Start processes
CMD ["/usr/bin/supervisord"]

EXPOSE 80 443
