################################################################
# Dockerfile to deploy a nginx caching 
# Based on Ubuntu 14.04
################################################################

# Setting the base image to Ubuntu 14.04
FROM ubuntu:14.04

MAINTAINER Alex Vaque

# Installing nginx
RUN apt-get -qq update && \
apt-get install -y nginx && \
apt-get install -y tar git curl nano wget dialog net-tools build-essential
# Install Python and Basic Python Tools
RUN apt-get install -y python python-dev python-distribute python-pip


# Cleaning caches
RUN rm -rf /var/lib/apt/lists/* && \
sudo apt-get clean

# Install basic applications
# Copy the application folder inside the container
ADD /app /app
# Get pip to download and install requirements:
RUN pip install -r /app/requirements.txt


#Creating nginx cache directories
RUN mkdir -p /usr/share/nginx/cache/tmp

# Configuring nginx
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
COPY etc/nginx/sites-enabled/default /etc/nginx/sites-enabled/default 
COPY etc/nginx/conf.d/cachezone.conf /etc/nginx/conf.d/cachezone.conf
COPY ./app /app


# Set the default directory where CMD will execute
WORKDIR /app

# Set the default command to execute    
# when creating a new container
# i.e. using CherryPy to serve the application
#RUN python /app/web.py

# Run nginx on docker run
#CMD ["/usr/sbin/nginx", "-c", "/etc/nginx/nginx.conf"]
CMD ["/usr/sbin/nginx -c /etc/nginx/nginx.conf && /usr/bin/python /app/web.py"]
# Expose 80 port
EXPOSE 80



