from keras.models import load_model
import cv2
import numpy as np
from random import choice

REV_CLASS_MAP = {
    0 : "seratus",
    1 : "duaribu",
   
    2 : "none",
}

def mapper(val):
    return REV_CLASS_MAP[val]


model = load_model("model.h5")

cap = cv2.VideoCapture(1)

prev_move = None

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    if not ret:
        continue

    # rectangle for user to play
    cv2.rectangle(frame, (200, 100), (500, 400), (255, 255, 255), 2)
    # rectangle for computer to play
    cv2.rectangle(frame, (800, 100), (1200, 500), (255, 255, 255), 2)

    # extract the region of image within the user rectangle
    roi = frame[100:500, 100:500]
    img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    #gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (227, 227))
    # predict the move made
    pred = model.predict(np.array([img]))
    #accurat = pred[0]
    move_code = np.argmax(pred[0])
    user_move_name = mapper(move_code)
   
    score = float("%0.2f" % (max(pred[0]) * 100))
    # for (x, y, w, h) in model:
    #     # print(x,y,w,h)
    #     roi_gray = gray[y:y+h, x:x+w] #[cord1=height,cord2=height]
    #     roi_color = frame[y:y+h, x:x+w]
   # contours,hierarchy= cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


    if (score>=70):
        # for i in range(len( contours)):
        #     x,y,w,h=cv2.boundingRect(contours[i])
        #     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0), 2)
        #     #cv2.putText(frame,str(area),(x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 1 ,(0,0,255), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        # cv2.drawContours(frame,img,-1,(255,0,0),3)
        
        cv2.putText(frame,  user_move_name +" "+ str(score)+"%",
                    (50, 50), font, 1.2, (255, 255, 200), 2, cv2.LINE_AA)
    cv2.imshow("frame", frame)

    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
