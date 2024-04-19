import cv2
import track_hand as htm
import paho.mqtt.client as mqtt
import time  # Importați modulul time

cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.8, maxHands=1)

fingerTip = [4, 8, 12, 16, 20]
fingerVal = [0, 0, 0, 0, 0]
prevFingerVal = [0, 0, 0, 0, 0]  # Valorile de degete din frame-ul anterior
lastValidFingerVal = prevFingerVal[:]  # Ultima valoare validă a degetelor

broker = "broker.emqx.io"
topic = "ArduMeka/keren39493"
Client = mqtt.Client()
Client.connect(broker)

red = (0, 0, 255)
yellow = (0, 255, 255)
blue = (255, 0, 0)
green = (0, 255, 0)
purple = (255, 0, 255)

color = [red, yellow, blue, green, purple]

last_send_time = 0  # Variabilă pentru a urmări momentul ultimei trimiteri

while cap.isOpened():
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if lmList:
        # Thumb
        handType = detector.handType()
        if handType == "Right":
            if lmList[fingerTip[0]][1] > lmList[fingerTip[0] - 1][1]:
                fingerVal[0] = 1
            else:
                fingerVal[0] = 0
        else:
            if lmList[fingerTip[0]][1] < lmList[fingerTip[0] - 1][1]:
                fingerVal[0] = 1
            else:
                fingerVal[0] = 0

        # 4 fingers
        for i in range(1, 5):
            if lmList[fingerTip[i]][2] < lmList[fingerTip[i] - 2][2]:
                fingerVal[i] = 1
            else:
                fingerVal[i] = 0

        if fingerVal != prevFingerVal:
            lastValidFingerVal = fingerVal[:]  # Actualizează ultima valoare validă a degetelor
            prevFingerVal = fingerVal[:]  # Actualizează valorile de degete pentru frame-ul anterior
            current_time = time.time()  # Obține timpul curent
            if current_time - last_send_time > 1:  # Verifică dacă a trecut cel puțin 1 secundă de la ultima trimitere
                strVal = ''.join(map(str, fingerVal))
                print(fingerVal)
                Client.publish(topic, strVal)
                last_send_time = current_time  # Actualizează timpul ultimei trimiteri

    cv2.imshow("Imagine", img)
    cv2.waitKey(1)
