#!/usr/bin/env python
# -*- coding:utf8 -*-

# import the necessary packages
import math
import numpy as np
import cv2
import cv
import socket
import struct
from time import sleep
import multiprocessing as mul
import threading

# initialize the current frame of the video, along with the list of
# ROI points along with whether or not this is input mode

camera_port = 1
frame = None
roiPts = []
inputMode = False
sendMessage = True
target_x = -1
target_y = -1
robot_x = -1
robot_y = -1

def ConvertPosToDegree(src_x,src_y,des_x,des_y):
    offset = 90
    degree = math.degrees(math.atan2(des_y-src_y,des_x-src_x))
    if (degree < 0.0):
        degree += 360
    return degree

def SelectROI(event, x, y, flags, param):
    global frame, roiPts, inputMode,target_x,target_y

    if inputMode and event == cv2.EVENT_LBUTTONDOWN and len(roiPts) < 4:
        roiPts.append((x, y))
        cv2.circle(frame, (x, y), 4, (0, 255, 0), 2)
        cv2.imshow("frame", frame)
    #tag on capute screen point
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(frame,(x,y),100,(255,0,0),-1)
        target_x = x
        target_y = y



def Tracking():

    # grab the reference to the current frame, list of ROI
    # points and whether or not it is ROI selection mode
    global frame, roiPts, inputMode, robot_x, robot_y, sendMessage

    camera = cv2.VideoCapture(camera_port)

    # otherwise, load the video

    # setup the mouse callback
    cv2.namedWindow("frame")
    cv2.setMouseCallback("frame", SelectROI)
    #cv2.setMouseCallback("frame",draw_circle)

    termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
    roiBox = None

    # keep looping over the frames
    while True:
        (grabbed, frame) = camera.read()

        # check to see if we have reached the end of the
        # video
        if not grabbed:
            break

        # if the see if the ROI has been computed
        if roiBox is not None:
            #print roiBox
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            backProj = cv2.calcBackProject([hsv], [0], roiHist, [0, 180], 1)

            # apply cam shift to the back projection, convert the
            # points to a bounding box, and then draw them
            (r, roiBox) = cv2.CamShift(backProj, roiBox, termination)
            pts = np.int0(cv2.cv.BoxPoints(r))

            top_left_x = pts[0][0]
            top_left_y = pts[0][1]

            top_right_x = pts[1][0]
            top_right_y = pts[1][1]

            button_right_x = pts[2][0]
            button_right_y = pts[2][1]

            button_left_x = pts[3][0]
            button_left_y = pts[3][1]

            robot_x = top_left_x + abs(top_right_x - top_left_x)/2
            robot_y = top_left_y + abs(top_right_y - button_left_y)/2



            circle_size = 10
            #draw point on screen
            cv2.polylines(frame, [pts], True, (0, 255, 0), 2)
            cv2.circle(frame,(target_x,target_y),circle_size,(0,0,255),-1)
            cv2.circle(frame,(top_left_x,top_left_y),circle_size,(0,255,255),-1)
            cv2.circle(frame,(top_right_x,top_right_y),circle_size,(0,255,255),-1)
            cv2.circle(frame,(button_right_x,button_right_y),circle_size,(0,255,255),-1)
            cv2.circle(frame,(button_left_x,button_left_y),circle_size,(0,255,255),-1)
            cv2.circle(frame,(robot_x,robot_y),circle_size,(0,255,255),-1)
            cv2.line(frame,(target_x,target_y),(robot_x,robot_y),(255,0,0),5)


            robot_goal = ConvertPosToDegree(robot_x,robot_y,target_x,target_y)
            robot_goal = str(robot_goal)
            font = cv2.FONT_HERSHEY_SIMPLEX

            cv2.putText(frame,robot_goal,(50,50), font, 1,(255,255,0),2)


            #print "robot: " + repr(robot_x),repr(robot_y)
            #print "target: " + repr(target_x),repr(target_y)

        # show the frame and record if the user presses a key
        cv2.imshow("frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # handle if the 'i' key is pressed, then go into ROI
        # selection mode
        if key == ord("i") and len(roiPts) < 4:
            # indicate that we are in input mode and clone the
            # frame
            inputMode = True
            orig = frame.copy()

            # keep looping until 4 reference ROI points have
            # been selected; press any key to exit ROI selction
            # mode once 4 points have been selected
            while len(roiPts) < 4:
                cv2.imshow("frame", frame)
                cv2.waitKey(0)

            # determine the top-left and bottom-right points
            roiPts = np.array(roiPts)
            s = roiPts.sum(axis=1)
            tl = roiPts[np.argmin(s)]
            br = roiPts[np.argmax(s)]

            # grab the ROI for the bounding box and convert it
            # to the HSV color space
            roi = orig[tl[1]:br[1], tl[0]:br[0]]
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            #roi = cv2.cvtColor(roi, cv2.COLOR_BGR2LAB)

            # compute a HSV histogram for the ROI and store the
            # bounding box
            roiHist = cv2.calcHist([roi], [0], None, [16], [0, 180])
            roiHist = cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX)
            roiBox = (tl[0], tl[1], br[0], br[1])

        if key == ord("q"):
            sendMessage = False
            break

    # cleanup the camera and close any open windows
    camera.release()
    cv2.destroyAllWindows()


def SendToRobot():
    robot_address = '192.168.100.4'
    local_test = '127.0.0.1'
    address = (robot_address, 31500)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while sendMessage:
        robot_coordinate = struct.pack("ii",robot_x,robot_y)
        if not robot_coordinate:
            break
        s.sendto(robot_coordinate, address)
        sleep(0.3)
    s.close()

Tracking = threading.Thread(target=Tracking)
SendToRobot =threading.Thread(target=SendToRobot)
Tracking.start()
#SendToRobot.start()

