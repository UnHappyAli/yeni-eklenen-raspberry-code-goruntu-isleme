import cv2
import numpy as np


# Kamerayı başlat
cap = cv2.VideoCapture(0)

while True:
    # Kameradan görüntü al
    ret, frame = cap.read()

    # Görüntüyü BGR renk uzayından HSV renk uzayına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Mavi renklerin maskesini oluştur
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Mavi renklerin konturlarını bul
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)





    # Mavi renklerin içindeki dikdörtgenleri çiz
    for c in contours:
        x,y,w,h = cv2.boundingRect(c)
        if w > 50 and h > 50: # Dikdörtgen boyutunu kontrol et
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            first_dot_x = x
            first_dot_y = y
            second_dot_x = x + w
            second_dot_y = y
            third_dot_x = x
            third_dot_y =y+h
            fourth_dot_x = x + w
            fourth_dot_y=y+h


            print("A {}, {}, B,{}, {},C,{}, {},D,{}, {})".format(first_dot_x,first_dot_y,
                                                          second_dot_x,second_dot_y,
                                                          third_dot_x,third_dot_y,
                                                          fourth_dot_x,fourth_dot_y))

            




    # Görüntüyü ekrana göster
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı kapat
cap.release()
cv2.destroyAllWindows()