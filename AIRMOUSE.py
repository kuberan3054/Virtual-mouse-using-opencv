import cv2
import mediapipe as mp
import pyautogui
#we will change it to depth camera or IP camera afterward
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_x,index_y,ring_x,ring_y,mid_x,mid_y = 0,0,0,0,0,0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width,_= frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)


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
                    else:
                        pyautogui.moveTo(mid_x, mid_y)


    cv2.imshow('AIRMOUSE', frame)
    cv2.waitKey(1)
'''
1.frame size
2.right click
3.volume
4.scroll

'''
