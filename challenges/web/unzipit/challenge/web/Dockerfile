FROM php:8.0-apache-bullseye

RUN apt-get update && apt-get -y upgrade

RUN apt-get -y install \
    zlib1g \
    zlib1g-dev \
    unzip \
    libzip-dev


RUN docker-php-ext-install zip mysqli

COPY www/ /var/www/html


RUN chown www-data:www-data /var/www/html/*
RUN chmod -R 777 /var/www/html/archives


EXPOSE 80
