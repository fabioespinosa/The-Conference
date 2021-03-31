# # Dockerfile

# FROM python:3.6

# # install nginx
# # RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
# # COPY nginx.default /etc/nginx/sites-available/default
# # RUN ln -sf /dev/stdout /var/log/nginx/access.log \
# # && ln -sf /dev/stderr /var/log/nginx/error.log

# ENV DJANGO_DEBUG True
# WORKDIR /usr/src/app
# COPY requirements.txt /usr/src/app 
# RUN pip install -r requirements.txt

# COPY . .


# # start server
# EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Dockerfile
FROM python:3.6.8
WORKDIR /app
COPY requirements.txt /app/

RUN pip install -r requirements.txt 
RUN chmod -R 777 /app/
RUN mkdir media static logs

COPY . .
RUN python manage.py collectstatic --noinput
# RUN python manage.py runserver
EXPOSE 8000
STOPSIGNAL SIGINT
COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]