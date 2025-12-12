# a1 = float(input("Введіть 1 число: "))
# print("============================")
# a2 = float(input("Введіть 2 число: "))
# print("============================")
# a3 = int(input("""Введіть що вибрати:"
# "==========="
# "1 мінус"
# "==========="
# "2 плюс"
# "==========="
# "3 діленя"
# "==========="
# "4 множення """))

# if a3 == 1:
#     z = a1 - a2
    
# if a3 == 2:
#     z = a1 + a2

# if a3 == 3:
#     if a1 == 0:
#         print("========== На нуль не можно ділити ===========")
#     z = a1 / a2

# if a3 == 4:
#     z = a1 * a2

# print("========== Результат дії =========")


# print(z)

import cv2
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2,detectionCon=0.8)
while True:
     success,img = cap.read()
     hand,img = detector.findHands(img,draw=True) 
     # список руки --- [0,0,0,0,0]
     if hand:
        totalfingers = 0
        for hands in hand:
            fingers = detector.fingersUp(hands)
            totalfingers += fingers.count(1)
        cv2.putText(img,str(totalfingers),(50,150),cv2.FONT_HERSHEY_COMPLEX,10,(255,0,255),10)
        cv2.imshow("Finger counter",img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
