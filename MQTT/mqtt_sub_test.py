import paho.mqtt.client as mqtt

#Connection success callback
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
    client.subscribe('esp32/data_dht')

# Message receiving callback
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()

# Specify callback function (this callback will be called once client.connect() success to connect to the mqtt broker)
client.on_connect = on_connect
client.on_message = on_message

# Establish a connection
client.connect('broker.emqx.io', 1883, 60)
# first arg = broker address
# second arg = port
# third arg = "keep-alive" time
#       The MQTT protocol requires the client to periodically send a "ping" message to the broker to maintain the connection.
#        This parameter specifies how often the client should send these pings to keep the connection alive. In this case, it's set to 60 seconds.

client.loop_forever()  # a loop that continuously execute all callback functions again and again