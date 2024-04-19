import paho.mqtt.client as mqtt
import speech_recognition as sr

broker = "luceafarului20.go.ro"
port = 1883
username = "HS2024"
password = "HS2024@!"
topic = "homeassistant/switch/pcf_pin__4/state"

client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(broker, port)

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
            # Trimite comanda prin MQTT doar dacă este "light on"
            if command == "light on":
                client.publish(topic, "1")
            elif command == "light off":
                client.publish(topic, "0")
        except sr.UnknownValueError:
            print("Comanda nu a fost recunoscută. Încearcă din nou.")
        except sr.RequestError as e:
            print("Căutarea pentru serviciul de recunoaștere vocală a eșuat. Verifică conexiunea la internet.", e)
