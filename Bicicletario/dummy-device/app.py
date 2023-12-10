import random
import time
import json
import requests


from multiprocessing import Process, Value
from flask import Flask, request, make_response, json


SEND = Value('b', False)
INTERVAL = 5

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    print(f"request: {request.json}")
    return make_response(json.dumps({"on":"method executed"}), 200)

@app.route("/bic23", methods=['GET', 'POST'])
def bic23():
    if request.method == 'POST':
        data = request.json
        print(data)
        if "start" in data:
            if SEND.value == False:
                SEND.value = True
                return make_response(json.dumps({'start': 'BIC23 started'}), 200)
            elif SEND.value == True:
                return make_response(json.dumps({'start': 'BIC23 already started'}), 200)
            else:
                return make_response(json.dumps({'error': 'Method not allowed'}), 405)
        elif "stop" in data:
            if SEND.value == True:
                SEND.value = False
                return make_response(json.dumps({'stop': 'BIC23 stopped'}), 200)
            elif SEND.value == False:
                return make_response(json.dumps({'stop': 'BIC23 already stopped'}), 200)
            else:
                return make_response(json.dumps({'error': 'Method not allowed'}), 405)
        else:
            return make_response(json.dumps({'error': 'Method not allowed'}), 405)

# Function to save data in a csv file. Running from a thread.
def sendData():
    while True:
        if SEND.value:
            l = random.randint(1, 3)
            if l == 1:
                location = 'in'
            else:
                location = 'out'
            url = "http://fiware-iot-agent-json:7896/iot/json?k=4jggokgpepnvsb2uv4s40d59ov&i=bike001"
            payload = json.dumps({
                "location": location

            })

            headers = {
                'fiware-service': 'openiot',
                'fiware-servicepath': '/',
                'Content-Type': 'application/json'  
            }
            try:
                response = requests.request("POST", url, headers=headers, data=payload)
            except:
                print("Error sending the message")
            print(response.text)

        
        time.sleep(INTERVAL)

p = Process(target=sendData).start()

if __name__ == "__main__":
    sendData()
