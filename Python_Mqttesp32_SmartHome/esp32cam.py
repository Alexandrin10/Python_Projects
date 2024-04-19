import cv2
import requests
import numpy as np
import paho.mqtt.client as mqtt
import speech_recognition as sr

broker = "broker.emqx.io"
topic = "ArduMeka/keren39493" # Aici poți introduce topicul dorit

Client = mqtt.Client()
Client.connect(broker)

# Initializare recunoașterea vocii
recognizer = sr.Recognizer()

while True:
    # Ascultă comenzi vocale
    with sr.Microphone() as source:
        print("Ascultă comenzi...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print("Comanda detectată:", command)
            # Trimite comanda prin MQTT
            if command == "light on":
                Client.publish(topic, "1")
            elif command == "light off":
                Client.publish(topic, "0")
        except sr.UnknownValueError:
            print("Comanda nu a fost recunoscută. Încearcă din nou.")
        except sr.RequestError as e:
            print("Căutarea pentru serviciul de recunoaștere vocală a eșuat. Verifică conexiunea la internet.", e)
