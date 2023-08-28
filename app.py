import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe("text")  
    else:
        print("Connection failed")

def on_message(client, userdata, message):
    print(f"Received message on topic {message.topic}: {message.payload.decode()}")

def on_publish(client, userdata, mid):
    print(f"Message published (mid: {mid})")

client = mqtt.Client(client_id="123")  
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

broker_address = "192.168.1.245"  
port = 1883 

client.connect(broker_address, port=port, keepalive=60)

# client.loop_forever()

client.loop_start()

topic = "text"  
message = "Hello, MQTT! yopi" 

client.publish(topic, message)

time.sleep(1)  
client.disconnect()
client.loop_stop()
