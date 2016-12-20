#sudo docker-compose up
#/bin/bash

sudo bash -x build.sh

echo -e "Starting Docker Compose"
sudo ./run.py project init 
sudo ./run.py project start
sudo ./run.py project logs
