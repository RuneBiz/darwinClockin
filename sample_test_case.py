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
    website.get("https://cos.darwinbox.com/user/login")
    
    # Login Page
    time.sleep(2)
    darwin = website.find_element(By.ID, 'UserLogin_username')
    darwin.send_keys(MY_USERNAME)
    
    darwin = website.find_element(By.ID, 'UserLogin_password')
    darwin.send_keys(MY_PASSWORD)
    
    darwin_sign_in = website.find_element(By.ID, "login-submit")
    darwin_sign_in.click()
    
    time.sleep(2)
    
    skip = website.find_element(By.CLASS_NAME, 'skip_pulse')
    if skip.text != "":
        skip.click()
    
    # clockin
    clockin_btn = website.find_element_by_id('attendance-logger-widget')
    clockin_btn.click()
    time.sleep(2)
    
    #Signout
    website.get("https://cos.darwinbox.com/user/logout")
    time.sleep(1)
    
    #Close Chrome
    website.quit()
