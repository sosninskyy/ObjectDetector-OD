import cv2
import serial
import time

ser = serial.Serial('COM4', 9600) 
time.sleep(2) 



url = '' #Here you should make url in app ip webcam or something similiar
cap = cv2.VideoCapture(url)


ret, frame1 = cap.read()
ret, frame2 = cap.read()
last_state = '2'

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 2000: # if you wanna make detect EVERY object, change that number to 10 or 100
            continue
        

        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "STATUS: MOVEMENT", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        ser.write(b'1')
    cv2.imshow("Big brother watching u", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()