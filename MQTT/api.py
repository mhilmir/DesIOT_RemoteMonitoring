from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask.helpers import make_response
from flask.templating import render_template
from werkzeug.wrappers import response
import pandas as pd
import sqlConnector
import socket
import json
import paho.mqtt.client as mqtt

app = Flask(__name__, template_folder="template")
app.config["DEBUG"] = True
api = Api(app)

# untuk mendapatkan ip address
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

class ESP(Resource):
    def get(self):
        data = sqlConnector.getTodayData()
        data = pd.DataFrame(data, columns=["ID","Date","Temp"])
        data["Date"] = data["Date"].dt.strftime("%Y-%m-%d %H:%M:%S")
        data = data.to_dict('records')
        return {'data' : data}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('temperature', location="args", required=True)
        parser.add_argument('lokasi', required=False)
        args = parser.parse_args()

        new_data = pd.DataFrame({
            'temperature' : [args['temperature']],
            'lokasi'      : [args['lokasi']],
        })
        sqlConnector.postData(float(args['temperature']))
        return {'data' : new_data.to_dict('records')}, 201
        #http://192.168.43.95/esp?temperature=37.5&lokasi=surabaya

# Add URL endpoints
api.add_resource(ESP, '/esp')

# Setting MQTT callbacks 
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
    client.subscribe('esp32/data_dht')
def on_message(client, userdata, msg):
    sqlConnector.postData(float(msg.payload))

# home() will be called when user navigates to the root URL
@app.route("/")
def home():
    data = sqlConnector.getTodayData()
    data = pd.DataFrame(data, columns=["ID","Date","Temp"])
    data["Date"] = data["Date"].dt.strftime("%Y-%m-%d %H:%M:%S")
    labels = [row for row in data['Date']][::-1]
    values = [row for row in data['Temp']][::-1]
    return render_template(template_name_or_list='charts.html', label=labels, value=values)

# data() will be called when user navigates to /chartData endpoint
@app.route("/chartData")
def data():
    data = sqlConnector.getLastData()
    data = pd.DataFrame(data, columns=["ID","Date","Temp"])
    data["Date"] = data["Date"].dt.strftime("%Y-%m-%d %H:%M:%S")
    data = [data["Date"][0], data["Temp"][0]]
    print(data)
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect('broker.emqx.io', 1883, 60)
    client.loop_start()
    app.run(host=f"{get_local_ip()}")