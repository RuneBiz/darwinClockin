from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
import time
import os

def test_login_fail_with_wrong_credentials():

    MY_USERNAME = os.environ["MY_USERNAME"]
    MY_PASSWORD = os.environ["MY_PASSWORD"]
    
    website = webdriver.Chrome()
    website.get("https://cos.darwinbox.com")
    
    time.sleep(2)
    username_field = website.find_element(By.ID, 'UserLogin_username')
    username_field.send_keys(MY_USERNAME)
    password_field = website.find_element(By.ID, 'UserLogin_password')
    password_field.send_keys(MY_PASSWORD)
    
    password_field.send_keys(Keys.RETURN)
    time.sleep(2)
    
    skip = website.find_element(By.CLASS_NAME, 'skip_pulse')
    if skip.text != "":
        skip.click()
    
    # clockin
    clockin_btn = website.find_element_by_id('attendance-logger-widget')
    clockin_btn.clear()
    time.sleep(2)
    
    #Signout
    driver.get('https://cos.darwinbox.com' + "/user/logout")
    time.sleep(1)
    
    #Close Chrome
    driver.quit()
    
    print('berhasil yes') 
