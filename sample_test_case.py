from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
import time


def test_home_page():
    website = webdriver.Chrome()
    website.get("https://www.facebook.com/")
    
    # page load check
    # if website was loaded, test will be passed.
    assert "Facebook – log in or sign up" in website.title
    
    website.close()


def test_login_fail_with_fake_credentials():
    website = webdriver.Chrome()
    website.get("https://www.facebook.com/")

    # add wrong username
    website_login_email = website.find_element(By.NAME, "email")
    website_login_email.send_keys("wronguser@email.com")

    # add wrong password
    website_login_password = website.find_element(By.NAME, "pass")
    website_login_password.send_keys("wrongpassword")

    # login with fake credentials
    website_login_button = website.find_element(By.NAME, "login")
    website_login_button.click()

    time.sleep(10)

    # getting current URL source code
    get_website_current_source = website.page_source

    # login fail check
    # if login fail, test will be passed.
    assert "Invalid username or password" in get_website_current_source

    website.close()
