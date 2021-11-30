import socket
import sys

HOST = None
PORT=50007
s = None

for res in socket.getaddrinfo(HOST,PORT,socket.AF_UNSPEC,socket.SOCK_STREAM,0,socket.AI_PASSIVE):
    af,socktype, proto , cononnamme,sa = res
    try:
        s = socket.socket(af,socktype,proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.bind(sa)
        s.listen(5)
    except OSError as msg:
        s.close()
        s = None
        continue
    break

if s is None:
    print("Cannot establish connection")
    sys.exit(5)
    
conn,addr = s.accept()
with conn:
    print("Connected with ",addr)
    while True:
        data = conn.recv(1024)
        
        if not data :
            break
        conn.send(data) 
