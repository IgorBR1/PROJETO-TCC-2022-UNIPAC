import cv2
import pickle
import cvzone
import numpy as np

cap = cv2.VideoCapture("car_par2.mp4") #comentario para trocar para video mp4
#cap = cv2.VideoCapture(0) #video webcam/camera


with open("TESTE2","rb") as c:
    posList = pickle.load(c)

largura, altura = 90, 55
print(len(posList))
def detect_car( imgPro):
    contador = 0

    for pos in posList:

        x, y, largura, altura = pos

        imgCrop = imgPro[
            y:y + altura,
            x:x + largura
        ]

        count = cv2.countNonZero(imgCrop)

        if count < 50:
            color = (0, 255, 0)
            contador += 1
        else:
            color = (0, 0, 255)

        cv2.rectangle(
            img,
            (x, y),
            (x + largura, y + altura),
            color,
            2
        )

        cvzone.putTextRect(
            img,
            str(count),
            (x, y + altura - 3),
            scale=1,
            thickness=2,
            offset=10,
            colorR=color
        )

    cvzone.putTextRect(
        img,
        f"Vagas abertas: {contador}/{len(posList)}",
        (120, 30),
        scale=2,
        thickness=5,
        offset=20,
        colorR=(0, 155, 0)
    )
while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    teste, img = cap.read()

    imgGray = cv2.cvtColor( img , cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)


    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 19)

    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3,3), np.uint8)
    img_dilate = cv2.dilate(imgMedian,kernel,iterations=1)






    detect_car(img_dilate)
    cv2.imshow("video",img)
    cv2.imshow("Video Blur", imgBlur)
    cv2.imshow("Video Treshold",imgThreshold)

    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
    
    
