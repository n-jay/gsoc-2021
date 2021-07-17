import requests
from time import time, sleep

print("Sending request...");

def sendRequest():
    r = requests.get('http://synapse-service:8280/backend');
    print(r.status_code);
    print(r.text);

while True:
    sleep(10 - time() % 10)
    sendRequest();
