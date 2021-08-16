FROM openjdk:8
# COPY /synapse-3.0.2-SNAPSHOT /usr/src/synapse
COPY /synapse /usr/src/synapse
WORKDIR /usr/src/synapse
EXPOSE 9000 
CMD [ "sh", "samples/axis2Server/axis2server.sh"]