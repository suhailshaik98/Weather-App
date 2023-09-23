FROM ubuntu:22.04

####Installing Node 18.x
RUN apt-get update && apt-get install -y curl
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get update \
    && apt-get install -y nodejs python3 python3-pip
RUN apt-get install -y redis-server

#### Git Dependencies
RUN apt-get install -y git jq
COPY token token
RUN export token=`cat token`
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN git clone https://$token@github.com/suhailshaik98/Weather-App.git
# COPY /root/Weather-App Weather-App
RUN cd Weather-App/react-frontend/ && npm install
COPY ip_address.sh ip_address.sh

# ENTRYPOINT ["Weather-App/python3 manage.py runserver","Weather-App/react-frontend/npm start"]
ENTRYPOINT cd Weather-App/ && python3 manage.py runserver 0.0.0.0:8000 & cd Weather-App/react-frontend/ && npm start
