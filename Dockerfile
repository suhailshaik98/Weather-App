FROM ubuntu:22.04

#####Environment variables######


RUN export req=""

####Installing Node 18.x
RUN apt-get update && apt-get install -y curl
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get update \
    && apt-get install -y nodejs python3 python3-pip
RUN mkdir Weather-App
#### Git Dependencies
COPY . Weather-App/
# COPY /root/Weather-App Weather-App
COPY dockercontainer/requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN cd Weather-App/react-frontend/ && npm install
RUN cd Weather-App/react-frontend/ && chmod +x ip_address_updater.sh
COPY dockercontainer/ip_address.sh ip_address.sh

# ENTRYPOINT ["Weather-App/python3 manage.py runserver","Weather-App/react-frontend/npm start"]
ENTRYPOINT cd Weather-App/react-frontend/ && ./ip_address_updater.sh src/App.js $req & cd Weather-App/ && python3 manage.py runserver 0.0.0.0:8000 & cd Weather-App/react-frontend/ && npm start 
