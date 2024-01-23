import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0) #You can change it to IP camera but there's a latency issue!
hand_detector = mp.solutions.hands.Hands() #This line will detect our had
drawing_utils = mp.solutions.drawing_utils # This Draws the colors on landmarks
screen_width, screen_height = pyautogui.size() 
index_x,index_y,ring_x,ring_y,mid_x,mid_y,thumb_x,thumb_y = 0,0,0,0,0,0,0,0 #initial condition

while True:
    
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width,_= frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # As we all know CV2 reads in BGR format so we are changing it to RGB for processing.
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)

                if id ==4: # if you count the landmarks thumb finger's tip is the 4th point 
                    
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(255, 255, 255), thickness=2)
                    thumb_x  = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y
                    

                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 0),thickness=2)
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y

                if id == 12:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 0,255 ),thickness=2)
                    mid_x = screen_width/frame_width*x
                    mid_y = screen_height/frame_height*y

                if id == 16:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(255, 0, 0), thickness=2)
                    ring_x = screen_width / frame_width * x
                    ring_y = screen_height / frame_height * y




                    if abs(mid_y - index_y) >100:
                        pyautogui.click()
                        pyautogui.sleep(1)
                        print("SINGLE CLICK : ",mid_y - index_y)
                    elif abs(mid_y - ring_y) > 100:
                        pyautogui.click(button='right')
                        pyautogui.sleep(1)
                        print("Right click ",mid_y-ring_y)

                    elif thumb_x - mid_x > 0 and thumb_x - mid_x < 110:
                        print("scrolling up")
                        pyautogui.scroll(150)
                    elif thumb_x - mid_x < 0 and thumb_x - mid_x >= -110:
                        print("scrolling down")
                        pyautogui.scroll(-150)

                    elif thumb_y-ring_y > -5 and thumb_y-ring_y < 70:
                        pyautogui.press('volumeup')

                    elif thumb_y-ring_y < -5 and thumb_y-ring_y >-70:
                        pyautogui.press('volumedown')

                    else:
                        pyautogui.moveTo(mid_x, mid_y)
                        
    cv2.imshow('AIRMOUSE', frame)
    cv2.waitKey(1)
'''
note :  
This is a very basic prototype and there are some drawbacks here
    i) you can't access you'r taskbar unless you have you taskbar associated on left or top of your screen.
    ii) you can't Double click or drag with this.
    iii)This code will detect all the hands in the screen .
    iv) you need to keep your hand straight with respect to the screen.
'''
