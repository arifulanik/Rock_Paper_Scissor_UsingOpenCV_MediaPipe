import cv2
import HandTrackingModule as htm
import time
import random

wCam,hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

pTime = 0
cTime = 0

detector = htm.handDetector()
player_prev_move = ""
com_prev_move = ""

while True :
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    player = ""
    computer = ""
    result = ""
    lst=[0,1,2]

    if len(lmList) != 0 :
        if lmList[8][2] < lmList[6][2] and lmList[12][2] < lmList[10][2] and lmList[16][2] > lmList[14][2]  and lmList[20][2] > lmList[18][2] :
            player = "Scissor"
        elif lmList[8][2] < lmList[6][2] and lmList[12][2] < lmList[10][2] and lmList[16][2] < lmList[14][2]  and lmList[20][2] < lmList[18][2] :
            player = "Paper"
        elif lmList[8][2] > lmList[6][2] and lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2]  and lmList[20][2] > lmList[18][2] :
            player = "Rock"
        else :
            player = "None"
    
    # game logic
    triger=random.randint(0,2)

    if triger==0:
        computer="Rock"
    elif triger==1:
        computer="Paper"
    else:
        computer="Scissor"
    
    if player_prev_move == player :
        computer = com_prev_move

    # check for draw
    if computer==player:
        result = "Draw"
    # player==Rock
    elif player=="Rock":
        if computer=="Paper":
            result = "Computer win"
        else:
            result = "Player win"
    #player==Paper
    elif player=="Paper":
        if computer=="Scissor":
            result = "Computer win"
        else:
            result = "Player win"
    #player==Scissor
    elif player=="Scissor":
        if computer=="Rock":
            result = "Computer win"
        else:
            result = "Player win"
    else:
        result = "Cant determine"
    # game logic end

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'computer: {computer}', (10,50), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,255), 3)
    cv2.putText(img, f'you: {player}', (10,80), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,255), 3)
    cv2.putText(img, f'result: {result}', (10,110), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

    player_prev_move = player
    com_prev_move = computer
