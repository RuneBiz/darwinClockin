from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
import time

def test_login_fail_with_wrong_credentials():
    website = webdriver.Chrome()
    website.get("https://connectosclockin.hrhub.ph/WebBundy")

    time.sleep(2)
    # add wrong username
    website_login_email = website.find_element('id', "Username")
    website_login_email.send_keys("rballesta")
        
    # add wrong password
    website_login_password = website.find_element('id', "Password")
    website_login_password.send_keys("enurFrost**1")
    
    # login with fake credentials
    website_login_button = website.find_element('id', "showCount")
    website_login_button.click()
    
    time.sleep(10)
    
    website.close()
