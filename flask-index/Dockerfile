FROM tiangolo/uwsgi-nginx-flask:flask

# Update the sources list
RUN apt-get update
# Install basic applications
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential
# Install Python and Basic Python Tools
RUN apt-get install -y python python-dev python-distribute python-pip

# Get pip to download and install requirements:
RUN pip install redis flask uwsgi 

#Creating nginx cache directories
RUN mkdir -p /usr/share/nginx/cache/tmp

# Add app configuration to Nginx
COPY etc/nginx/conf.d/nginx.conf /etc/nginx/conf.d/
COPY etc/nginx/conf.d/cachezone.conf /etc/nginx/conf.d/cachezone.conf


# Copy sample app
COPY ./app /app
