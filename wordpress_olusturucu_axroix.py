import sys
import os
def banner():
    print("""

    CREACTED BY 4XROIX : WORDLIST OLUSTURUCU

    """)
def olustur(ad='',soyad='',dogum_t='',sev_ad=''):
    ad = raw_input("HEDEFIN ADI : ")
    soyad = raw_input("HEDEFIN SOYADI : ")
    dogum_t = raw_input("HEDEFIN DOGUM TARIHI : ")
    sev_ad = raw_input("HEDEFIN SEVGISILININ ADI : ")
    f = open("password.list",'w')
    bilgiler = [ad,soyad,dogum_t,sev_ad]
    sayi = ['1234567890']
    bilgiler +=sayi
    passwd = []
    for d in bilgiler:
        passwd.append(d.lower())
    for d in bilgiler:
        for d2 in bilgiler:
           passwd.append(d.lower()+d2.lower())
           passwd.append(d.lower()+"."+d2.lower())
    for d in bilgiler:
        for d2 in bilgiler:
            for d3 in bilgiler:
                passwd.append(d.lower()+d2.lower()+d3.lower())
                passwd.append(d.lower()+"."+d2.lower()+"."+d3.lower())
    f.write("\n".join(passwd))
    f.close()
    print("Islem Tamam [+] - REDROOM SIKER")
banner()
olustur()