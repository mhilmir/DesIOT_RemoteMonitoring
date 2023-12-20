from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd
import sqlConnector
import socket

app = Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)

# untuk mendapatkan ip address
def get_local_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("ip_address:", ip_address)
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
        parser.add_argument('temperature', location="args", required=True)  # harus ditambahkan location="args" agar reqparse hanya search dari query params
        args = parser.parse_args()
        
        new_data = pd.DataFrame({
            'temperature' : [args['temperature']],
        })
        sqlConnector.postData(float(args['temperature']))
        return {'data' : new_data.to_dict('records')}, 201

# Add URL endpoints
api.add_resource(ESP, '/esp')

if __name__ == '__main__':
    app.run(host=f"{get_local_ip()}")