import socket
import struct
from time import sleep

robot_address = '192.168.100.3'
local_test = '127.0.0.1'
address = (robot_address, 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

x,y = 3,4

while True:

    pos = struct.pack("ii",x,y)
    x+=1
    y+=1
    msg = raw_input()
    if not msg:
        break
    s.sendto(msg, address)
    sleep(0.3)

s.close()

