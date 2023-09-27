echo "Removing existing zip files"
sudo rm -rf cidcd.zip
echo "Installing docker.io and docker compose"
sudo apt install -y docker.io
sudo apt-get install docker-compose-plugin
echo "Loading the docker container"
unzip cicd.zip
sudo docker load -i weatherapp.tar
echo "Stopping any instances of the docker"
sudo docker compose down
echo "Making the docker compose up"
docker compose up
