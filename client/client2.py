import requests
from time import time, sleep

print("Sending request...");

def sendRequest():
    r = requests.get('http://server:3000');
    print(r.status_code);
    print(r.text);

while True:
    sleep(10 - time() % 10)
    sendRequest();
