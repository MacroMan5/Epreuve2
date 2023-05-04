FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y apache2 && \
    apt-get clean

RUN a2enmod ssl

COPY ./html /var/www/html
COPY ./ssl /etc/ssl

RUN chown -R www-data:www-data /var/www/html

EXPOSE 80
EXPOSE 443

CMD ["apachectl", "-D", "FOREGROUND"]
