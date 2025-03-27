from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from flask import Flask,render_template,request
import tm
import time
import random
import base64

def sel(xq):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled") 
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver=webdriver.Chrome(options=options)
    url="https://www.google.com.tr/?hl=tr"
    driver.get(url)
    driver.maximize_window()
    search_box=driver.find_element(By.CLASS_NAME,'gLFyf')
    for letter in xq:
        search_box.send_keys(letter)
    time.sleep(random.randint(1, 5)/10) 
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    
    
    
    search_box2=driver.find_element(By.XPATH,'//*[@id="hdtb-sc"]')
    
    if search_box2.accessible_name=='Görseller':
        search_box2.send_keys(Keys.RETURN)
    else:
        search_box3=driver.find_element(By.XPATH,'//*[@id="hdtb-sc"]')
        search_box3.send_keys(Keys.RETURN)

    selected_image=driver.find_element(By.XPATH,'/html/body/div[3]/div/div[14]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[1]/div[2]/h3/a/div/div/div/g-img/img')
    img = base64.b64decode(selected_image.screenshot_as_base64)   
    with open(f"./static/img/a.png", "wb") as file:
        file.write(img)

            
    selected_image2=driver.find_element(By.XPATH,'/html/body/div[3]/div/div[14]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[2]/div[2]/h3/a/div/div/div/g-img/img')
    img2=base64.b64decode(selected_image2.screenshot_as_base64)
    with open(f"./static/img/b.png", "wb") as file:
        file.write(img2)





    selected_image3=driver.find_element(By.XPATH,'/html/body/div[3]/div/div[14]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[4]/div[2]/h3/a/div/div/div/g-img/img')
    img3=base64.b64decode(selected_image3.screenshot_as_base64)
    with open(f"./static/img/c.png", "wb") as file:
        file.write(img3)




if __name__=='__main__':
    sel('lebron')

