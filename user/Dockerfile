FROM python:3.8-buster

COPY install-nginx.sh /

RUN bash /install-nginx.sh

RUN pip install uwsgi

RUN rm /etc/nginx/conf.d/default.conf && rm /install-nginx.sh

COPY uwsgi.ini /etc/uwsgi/
COPY nginx.conf /etc/nginx/nginx.conf
COPY daemon.nginx.conf /etc/nginx/conf.d/nginx.conf

# Install Supervisord
RUN apt-get update && apt-get install -y supervisor \
    && rm -rf /var/lib/apt/lists/*
# Custom Supervisord config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80

RUN pip install flask

COPY ./app /app
WORKDIR /app
ENV PYTHONPATH=/app

ENTRYPOINT ["/usr/bin/supervisord"]
