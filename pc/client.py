#!/usr/bin/env python
# encoding: utf-8

## Color Tracking v1.0
## Copyright (c) 2013-2014 Abid K and Jay Edry
## You may use, redistribute and/or modify this program it under the terms of the MIT license (https://github.com/abidrahmank/MyRoughWork/blob/master/license.txt).

import math
import cv2
import numpy as np
import socket
import struct

#network
robot_address = '192.168.100.3'
local_test = '127.0.0.1'
address = (robot_address, 31500)
p_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

f = None
send_data = True
target_point_size = 8
target_x = -1
target_y = -1
robot_x = -1
robot_y = -1

def get_target_goal(src_x,src_y,des_x,des_y):
    degree = math.degrees(math.atan2(des_y-src_y,des_x-src_x))
    if (degree < 0.0):
        degree += 360
    return degree

def getthresholdedimg(hsv):
    yellow = cv2.inRange(hsv,np.array((20,100,100)),np.array((30,255,255)))
    blue = cv2.inRange(hsv,np.array((100,100,100)),np.array((120,255,255)))
    both = cv2.add(yellow,blue)
    # both = cv2.add(yellow)
    return both

def select_target(event, x, y, flags, param):
    global f,target_x,target_y
    #tag on capute screen point
    if event == cv2.EVENT_LBUTTONDBLCLK:
        target_x = x
        target_y = y
        robot_goal = get_target_goal(robot_x,robot_y,target_x,target_y)
        robot_goal = str(robot_goal)
        robot_goal = robot_goal.split('.')
        robot_goal = robot_goal[0]

        s_data = 'goal,' + robot_goal
        p_socket.sendto(s_data,address)
        print s_data


def tracking(camera_port=0):
    robot_origin_x,robot_origin_y = 0,0
    robot_move_x,robot_move_y = 0,0
    str_offset = "null"

    global f, robot_x, robot_y, send_data ,target_x,target_y
    c = cv2.VideoCapture(camera_port)
    cv2.namedWindow("f")
    cv2.setMouseCallback("f", select_target)
    width,height = c.get(3),c.get(4)
    print "frame width and height : ", width, height



    while(1):
        _,f = c.read()
        f = cv2.flip(f,1)
        blur = cv2.medianBlur(f,5)
        hsv = cv2.cvtColor(f,cv2.COLOR_BGR2HSV)
        both = getthresholdedimg(hsv)
        erode = cv2.erode(both,None,iterations = 3)
        dilate = cv2.dilate(erode,None,iterations = 10)
        contours,hierarchy = cv2.findContours(dilate,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        cv2.circle(f,(target_x,target_y),target_point_size,(0,0,255),-1)

        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            cx,cy = x+w/2, y+h/2
            robot_x,robot_y = cx,cy
            if 20 < hsv.item(cy,cx,0) < 30:
                pass
                # cv2.rectangle(f,(x,y),(x+w,y+h),[0,255,255],2)
                # print "yellow :", x,y,w,h
            elif 100 < hsv.item(cy,cx,0) < 120:
                cv2.line(f,(target_x,target_y),(robot_x,robot_y),(255,0,0),2)
                cv2.circle(f,(cx,cy),target_point_size,(0,255,255),-1)
                cv2.line(f,(robot_origin_x,robot_origin_y),(robot_move_x,robot_move_y),(255,200,0),2)
                robot_goal = get_target_goal(robot_x,robot_y,target_x,target_y)
                robot_goal = str(robot_goal)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(f,robot_goal,(50,50), font, 1,(255,255,0),2)
                cv2.putText(f,str_offset,(50,100), font, 1,(255,200,0),2)
                # cv2.rectangle(f,(x,y),(x+w,y+h),[255,0,0],2)
                # print "blue :", x,y,w,h
        cv2.imshow('f',f)
        k = cv2.waitKey(25)
        if k == 27:
            break
        elif k == ord('z'):
            robot_origin_x,robot_origin_y = robot_x,robot_y
            print "get robot origin point"
            print robot_origin_x,robot_origin_y
            p_socket.sendto('sync',address)
        elif k == ord('x'):
            robot_move_x,robot_move_y = robot_x,robot_y
            offset = get_target_goal(robot_origin_x,robot_origin_y,robot_move_x,robot_move_y)
            str_offset = str(offset)
            data_offset = 'offset,' + str_offset
            p_socket.sendto(data_offset,address)
            print "diff angle : " + str_offset
        elif k == ord('c'):
            p_socket.sendto('exit',address)







    cv2.destroyAllWindows()
    c.release()

tracking(0)
