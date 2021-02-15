# User service

Docker container running Flask and uwsgi on an Nginx server. Based on a well known and widely used pattern, combining uWSGI and Nginx to serve Python web applications.

The Flask application is served by `uwsgi`, based on the [uwsgi.ini](api/uwsgi.ini) file in the `api` folder. 


## uWSGI configuration

There is an order of loading uWSGI configurations, combining both `.ini` files and environment variables.

