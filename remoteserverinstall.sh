echo "Installing docker.io and docker compose"
sudo apt install -y docker.io
sudo apt  install -y docker-compose
sudo docker load -i weatherapp.tar
echo "Stopping any instances of the docker"
mv ~/dockercontainer/docker-compose.yml ~/docker-compose.yml
sudo docker-compose down
echo "Making the docker compose up"
sudo docker-compose up
