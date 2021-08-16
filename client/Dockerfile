# FROM python:3
FROM openjdk:8
# RUN pip install requests
RUN apt-get update
RUN apt-get install -y curl
# EXPOSE 3001
# ADD client2.py / 
# CMD [ "python3", "./client2.py" ]
COPY /synapse /usr/src/synapse
WORKDIR /usr/src/synapse/samples/axis2Client
