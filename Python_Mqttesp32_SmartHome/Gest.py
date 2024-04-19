import cv2
import track_hand as htm
import paho.mqtt.client as mqtt

cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.8, maxHands=1)

fingerTips = [4, 8, 12, 16, 20]

broker = "luceafarului20.go.ro"
port = 1883
username = "HS2024"
password = "HS2024@!"
topic = "homeassistant/switch/pcf_pin__4/state"

Client = mqtt.Client()
Client.username_pw_set(username, password)

while cap.isOpened():
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if lmList:
        # Inițializare starea degetelor
        fingersState = [0] * 5

        # Verifică starea fiecărui deget
        for i in range(5):
            if lmList[fingerTips[i]][2] < lmList[fingerTips[i] - 2][2]:  # Verificare coordonata Z pentru fiecare deget
                fingersState[i] = 1

        # Verifică dacă toate degetele sunt deschise sau nu
        if all(fingersState):
            handState = 1  # Toate degetele sunt deschise, LED-ul rămâne aprins (1)
        else:
            handState = 0  # Cel puțin un deget este închis

        # Trimitere starea mâinii către brokerul MQTT
        Client.connect(broker, port)
        Client.publish(topic, str(handState))
        Client.disconnect()

        # Desenare puncte pe degete pentru a vizualiza starea
        for i in range(5):
            if fingersState[i] == 1:
                cv2.circle(img, (int(lmList[fingerTips[i]][0]), int(lmList[fingerTips[i]][1])), 15, (0, 255, 0), cv2.FILLED)
            else:
                cv2.circle(img, (int(lmList[fingerTips[i]][0]), int(lmList[fingerTips[i]][1])), 15, (0, 0, 255), cv2.FILLED)

    cv2.imshow("Imagine", img)
    cv2.waitKey(1)
