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
    website.get("https://connectosclockin.hrhub.ph/WebBundy")
    
    time.sleep(2)
    # add wrong username
    website_login_email = website.find_element(By.ID, "Username")
    website_login_email.send_keys(MY_USERNAME)
        
    # add wrong password
    website_login_password = website.find_element(By.ID, "Password")
    website_login_password.send_keys(MY_PASSWORD)
    
    # login with fake credentials
    website_login_button = website.find_element(By.ID, "showCount")
    website_login_button.click()
    
    time.sleep(10)
    
    website.close()
