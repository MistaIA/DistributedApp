import sys
import socket

HOST = "localhost"
PORT=50007
s = None

for res in socket.getaddrinfo(HOST,PORT,socket.AF_UNSPEC,socket.SOCK_STREAM):
    af,socktype, proto , cononnamme,sa = res
    try:
        s = socket.socket(af,socktype,proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except OSError as msg:
        s.close()
        s = None
        continue
    break

if s is None:
    print("Cannot establish connection")
    sys.exit(5)

with s:
    # liste = [12,12,54,87,765,78,45,987,56,543]
    # alt = liste[len(liste):]
    # if len(liste) == 1:
    #     data = s.recv(1024)
    #     print("recieved",repr(data))   
    # else :
    #     s.send(alt)
    s.sendall(b"b- LAPTOP-4C : 4 Cores 2.80 GHz")
    data = s.recv(1024)
print("Received", repr(data))    
