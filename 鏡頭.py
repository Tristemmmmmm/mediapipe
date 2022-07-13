
import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands  #手部模型
hands = mpHands.Hands() #CRTL+左鍵可看參數
mpDraw = mp.solutions.drawing_utils  #繪圖方法


while True:
    ret,img=cap.read()
    if ret:
        
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  #BGR轉RGB
        result=hands.process(imgRGB)                #偵測手掌
        #print(result.multi_hand_landmarks)
        imgHeight=img.shape[0]                       #設定高第0個值   
        imgWidth=img.shape[1]                       #設定寬第1個值 
        #cv2.line(img,(0,160),(640,160),(0,0,255),5)#(影像, 開始座標, 結束座標, 顏色, 線條寬度)   (((畫線區域 31 34 37
        #cv2.line(img,(0,320),(640,320),(0,0,255),5)
        
        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                #mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)#哪張圖,landmark點畫上去,連線  ((((骨架部分
                for i,lm in enumerate(handLms.landmark):
                    xPos=int(lm.x*imgWidth) #將原本座標數值比例(30行)*視窗寬高(18,19) 最後整數化坐標
                    yPos=int(lm.y*imgHeight)
                    #print(i,xPos,yPos)
                    #print(i,lm.x,lm.y)
                    if i==8 and yPos>350:#if keys[pygame.K_DOWN]:    i==8代表食指
                        cv2.circle(img,(xPos,yPos),20,(0,255,0),cv2.FILLED) #下
                    else:
                        if i==8 and yPos>200 and yPos<350:
                            cv2.circle(img,(xPos,yPos),30,(0,255,255),cv2.FILLED) #中
                    
                    if i==8 and yPos<200:
                        
                       cv2.circle(img,(xPos,yPos),40,(255,255,0),cv2.FILLED) #上
        
        cv2.imshow('img',img)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows() 