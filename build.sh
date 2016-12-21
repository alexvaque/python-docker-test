#/bin/bash

echo -e " Building Containers"

pushd flask-index/
sudo docker build -t flask-index .
popd

pushd redis-server/
sudo docker build -t redis-server . 
popd

pushd proxy/
sudo docker build -t proxy .
popd

pushd haproxy/
sudo docker build -t haproxy .
popd

pushd lb_nginx/
sudo docker build -t lb_nginx .
popd
