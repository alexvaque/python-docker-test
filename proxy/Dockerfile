################################################################
# Dockerfile to deploy a nginx caching 
# Based on Ubuntu 14.04
################################################################

# Setting the base image to Ubuntu 14.04
FROM ubuntu:14.04

MAINTAINER Alex Vaque

# Installing nginx
RUN apt-get -qq update && \
apt-get install -y nginx 
# Cleaning caches
RUN rm -rf /var/lib/apt/lists/* && \
sudo apt-get clean

#Creating nginx cache directories
RUN mkdir -p /usr/share/nginx/cache/tmp

# Configuring nginx
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
COPY etc/nginx/sites-enabled/default /etc/nginx/sites-enabled/default 
COPY etc/nginx/conf.d/cachezone.conf /etc/nginx/conf.d/cachezone.conf

# Run nginx on docker run
CMD ["/usr/sbin/nginx", "-c", "/etc/nginx/nginx.conf"]

# Expose 80 port
EXPOSE 80
