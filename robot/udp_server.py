import socket
import struct

address = ('192.168.100.3', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

while True:
    data, addr = s.recvfrom(2048)
    x,y = struct.unpack("ii",data)
    if not data:
        print "client has exist"
        break
    #print "received:", data, "from", addr
    print x,y

s.close()

