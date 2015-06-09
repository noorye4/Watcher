#!/usr/bin/env python
# -*- coding:utf8 -*-
from time import sleep
from ev3.lego import *
from string import split

import serial
import threading
import random
import socket

#network
address = ('192.168.100.3', 31500)
r_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
r_socket.bind(address)

#sensor
touch_sensor = TouchSensor()

#motor
motor_A = LargeMotor(port='A')
motor_B = LargeMotor(port='B')
motor_A.stop_mode='hold'
motor_B.stop_mode='hold'
motor_power = 500


def forward(motor_power):
    motor_A.run_forever(motor_power,speed_regulation=True)
    motor_B.run_forever(motor_power,speed_regulation=True)

def back(motor_power):
    motor_A.run_forever(-motor_power,speed_regulation=True)
    motor_B.run_forever(-motor_power,speed_regulation=True)

def turn_left(motor_power):
    motor_A.run_forever(-motor_power,speed_regulation=True)
    motor_B.run_forever(motor_power,speed_regulation=True)

def turn_right(motor_power):
    motor_A.run_forever(motor_power,speed_regulation=True)
    motor_B.run_forever(-motor_power,speed_regulation=True)

def stop():
    motor_A.run_forever(0,speed_regulation=True)
    motor_B.run_forever(0,speed_regulation=True)


def rotate_compass():
    """
    turn Robot postive and nagtive 360 degree
    """
    """TODO: Docstring for rotate_compass.
    :returns: TODO

    """
    for i in range(3):
        turn_left(250)
        sleep(5)
        turn_right(250)
        sleep(5)
    stop()

def initial_serial():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    print "waiting serial initialization..."
    sleep(1)
    print "clear serial buffer..."
    ser.flushInput()
    ser.flushOutput()
    print "serial is open..."
    return ser

def commun_with_arduino(ser,t_rotate_compass):

    if ser.isOpen():
        print  "Please send cmd to arduino"
        print """
        Please input 0~5 number

        0: test ardunio and ev3 communiications
        1: First Start need Calibration Compass ; Start Calibration
        2: Setting Arduino Compass Base Angle
        3: Send Arduino Sensor data include IR and Compass
        4: Stop Send data
        5: quit

        """
        while True:
            cmd = raw_input(">> ")
            ser.write(cmd)
            if cmd == "5":
                print "exit commun_with_arduino"
                break

            while True:
                msg =  ser.readline()
                if msg == "hello arduino\r\n":
                    break
                if msg == "compass_calibration_start\r\n":
                    t_rotate_compass.start()
                    while 1:
                        msg =  ser.readline()
                        print msg
                        if msg == "compass_calibration_finsh\r\n":
                            break
                    break
                if msg == "setting_compass_base_angle\r\n":
                    break
                if msg == "start_send_data\r\n":
                    ser.flushOutput()
                    break
                if msg == "stop_send_data\r\n":
                    ser.flushOutput()
                    break

def read_sensor_data(ser):
    """
    sensor value index
    final_data[0] = current_degree
    final_data[1] = front_distance
    final_data[2] = left_distance
    final_data[3] = right_distance
    """
    if ser.isOpen():
        ser.flushOutput()
        raw_data = ser.readline().strip('\n')
        strip_data = raw_data.strip('\r')
        split_data = strip_data.split(',')
        while '' in split_data:
            split_data.remove('')
        if len(split_data) > 3:
            final_data = map(int,split_data)
            return final_data

def read_curr_angle(ser):
    sensor_data = read_sensor_data(ser)
    if sensor_data:
        current_degree = sensor_data[0]
        # print current_degree
    return current_degree


def convert_angle(current_degree):
    if current_degree > 180:
        current_degree -= 360
    return current_degree

def turn_to_goal(ser,r_socket):
    goal_degree = 90
    motor_power = 0
    Kp = 2
    while 1:
        # goal_degree_data, addr = r_socket.recvfrom(2048)
        # if goal_degree_data:
            # goal_degree_data = goal_degree_data.split(',')
            # if (goal_degree_data[0] == 'goal'):
                # goal_degree = goal_degree_data[1]
                # goal_degree = int(goal_degree)
                # print "goal_degree :",goal_degree

        sensor_data = read_sensor_data(ser)
        if sensor_data:
            current_degree = sensor_data[0]
            # current_degree = current_degree + compass_offset
            current_degree = convert_angle(current_degree)
            error = current_degree - goal_degree
            # print current_degree
            if abs(error) < 10:
                stop()
            else:
                z = current_degree + 180
                if error > z:
                    error -=180
                turn = error * Kp
                power_L = motor_power - turn
                power_R = motor_power + turn
                # print power_L,power_R,error
                print error
                motor_A.run_forever(power_L,speed_regulation=True)
                motor_B.run_forever(power_R,speed_regulation=True)
        if (touch_sensor.is_pushed):
            stop()
            r_socket.close()
            print "exit "
            break

def straight_to_goal(ser,goal_degree):
    # goal_degree = 180
    integral = 0
    derivative = 0
    last_error = 0
    memory_length = 0.5
    motor_power = 400
    Kp = 3
    Ki = 5
    Kd = 3
    while 1:
        sensor_data = read_sensor_data(ser)
        if sensor_data:
            current_degree = sensor_data[0]
            print current_degree
            error = current_degree - goal_degree
            if abs(error) <= 2:
               forward(400)
            else:
                z = current_degree + 180
                if error > z:
                    error -=180
                integral = memory_length * integral + error
                derivative = error - last_error
                turn = Kp * error + Ki * integral + Kd * derivative
                last_error = error
                turn = error * Kp
                power_L = motor_power - turn
                power_R = motor_power + turn
                motor_A.run_forever(power_L,speed_regulation=True)
                motor_B.run_forever(power_R,speed_regulation=True)
        if (touch_sensor.is_pushed):
            stop()
            print "exit "
            break


def boundary_following(ser,direction):
    #PID Control Parameters
    Kp = 1
    Ki = 5
    Kd = 4
    integral = 0
    derivative = 0
    last_error = 0
    memory_length = 0.5

    #Real world Robot Parameters
    offset = 30
    front_obstacle = 15
    motor_power = 400
    while 1:
        sensor_data = read_sensor_data(ser)
        if sensor_data:
            front_distance = sensor_data[1]
            left_distance = sensor_data[2]
            right_distance = sensor_data[3]
            # print left_distance,right_distance

            if direction == "left":
                error = left_distance - offset
                if front_distance < front_obstacle:
                    print "turn_right"
                    turn_right(400)
                else:
                    integral = memory_length * integral + error
                    derivative = error - last_error
                    turn = Kp * error + Ki * integral + Kd * derivative
                    last_error = error

                    if direction == "left":
                        power_L = motor_power - turn
                        power_R = motor_power + turn
                    if direction == "right":
                        power_L = motor_power + turn
                        power_R = motor_power - turn
                    motor_A.run_forever(power_L,speed_regulation=True)
                    motor_B.run_forever(power_R,speed_regulation=True)




            if direction == "right":
                error = right_distance - offset
                if front_distance < front_obstacle:
                    print "turn_right"
                    turn_left(400)
                else:
                    integral = memory_length * integral + error
                    derivative = error - last_error
                    turn = Kp * error + Ki * integral + Kd * derivative
                    last_error = error

                    if direction == "left":
                        power_L = motor_power - turn
                        power_R = motor_power + turn
                    if direction == "right":
                        power_L = motor_power + turn
                        power_R = motor_power - turn

                    motor_A.run_forever(power_L,speed_regulation=True)
                    motor_B.run_forever(power_R,speed_regulation=True)

        if (touch_sensor.is_pushed):
            stop()
            print "exit "
            break


def random_move(ser):
    front_obstacle = 30
    while 1:
        direction = random.randint(0,1)
        sensor_data = read_sensor_data(ser)
        if sensor_data:

            front_distance = sensor_data[1]
            if front_distance < front_obstacle:
                stop()
                back(400)
                sleep(1)
                if direction == 0:
                    print "left"
                    boundary_following(ser,"left")
                if direction == 1:
                    print "right"
                    boundary_following(ser,"right")
            else:
                print "forward"
                forward(400)

            if (touch_sensor.is_pushed):
                stop()
                print "exit "
                break

def sync_with_camera_coordinate(r_socket):
    print """
    Please press z key let car move straight
    then press x calc compass offset
    finally press c to quit
    """
    camera_degree = 0;
    exit = False
    while exit is not True:
        data, addr = r_socket.recvfrom(2048)
        if data:
            if data == 'sync':
                forward(250)
                sleep(1)
                stop()
            offset = data.split(',')
            if len(offset) == 2:
                camera_degree = offset[1]
                int_camera_degree = camera_degree.split('.')
                camera_degree = int_camera_degree[0]
            if data == 'exit':
                exit = True

        if (touch_sensor.is_pushed):
            r_socket.close()
            stop()
            print "exit "
            break
    camera_degree = int(camera_degree)
    print 'exit'
    return camera_degree

def recv_pc_cmd(r_socket):
    while True:
        data, addr = r_socket.recvfrom(2048)
        if data:
            print data
        if (touch_sensor.is_pushed):
            r_socket.close()
            stop()
            print "exit "
            break






# recv_pc_cmd(r_socket)

t_rotate_compass = threading.Thread(target=rotate_compass)
ser = initial_serial()
commun_with_arduino(ser,t_rotate_compass)
# camera_degree = sync_with_camera_coordinate(r_socket)
# current_degree = read_curr_angle(ser)
# print camera_degree,current_degree
# compass_offset = convert_compass(camera_degree,current_degree)
# print compass_offset
turn_to_goal(ser,r_socket)
# while 1:
    # current_degree = read_curr_angle(ser)
    # current_degree = convert_angle(current_degree)
    # print current_degree
    # if (touch_sensor.is_pushed):
        # stop()
        # print "exit "
        # break




#unit test
# boundary_following(ser,'right')
# boundary_following(ser,'left')
# turn_to_goal(ser)

