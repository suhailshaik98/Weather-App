echo "Installing docker.io and docker compose"
sudo apt install -y docker.io
sudo apt  install -y docker-compose
sudo docker load -i weatherapp.tar
echo "Stopping any instances of the docker"
cd dockercontainer && sudo docker-compose down
echo "Making the docker compose up"
cd dockercontainer && sudo docker-compose up
