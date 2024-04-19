import paho.mqtt.client as mqtt

broker = "luceafarului20.go.ro"
port = 1883
username = "HS2024"
password = "HS2024@!"
topic = "homeassistant/switch/pcf_pin__4/state" # Aici poți introduce topicul dorit

Client = mqtt.Client()
Client.username_pw_set(username, password)
Client.connect(broker, port)

while True:
    data = input("Introdu Data: ")
    Client.publish(topic, data)
    print(f'Data publicată: {data}')
