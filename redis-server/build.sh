sudo docker build -t redis-server . 
sudo docker run -d --name redis-server -p 6379:6379 redis-server


