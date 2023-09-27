echo "Installing docker.io and docker compose"
sudo apt install -y docker.io
sudo apt-get install docker-compose-plugin
sudo docker load -i weatherapp.tar
echo "Stopping any instances of the docker"
sudo docker compose down
echo "Making the docker compose up"
docker compose up
