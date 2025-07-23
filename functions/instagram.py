# instagram.py

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD

def init_driver(chromedriver_path: str):
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

def login(driver):
    try:
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        driver.find_element(By.NAME, "username").send_keys(INSTAGRAM_USERNAME)
        driver.find_element(By.NAME, "password").send_keys(INSTAGRAM_PASSWORD + Keys.RETURN)
        time.sleep(5)
        print("✅ Logged into Instagram.")
    except Exception as e:
        print("❌ Login failed:", e)
        raise

def start_livestream(driver, livestream_url):
    driver.get(livestream_url)
    time.sleep(5)
    try:
        driver.find_element(By.TAG_NAME, "body").click()
        print("🖱️ Clicked screen to activate stream.")
    except Exception as e:
        print("❌ Click failed:", e)
    time.sleep(20)

def post_comment(driver, comment: str):
    try:
        comment_box = driver.find_element(By.XPATH, "//textarea[@placeholder='Add a comment…']")
        comment_box.click()
        comment_box.send_keys(comment)
        time.sleep(1)
        comment_box.send_keys(Keys.RETURN)
        print("💬 Commented:", comment)
    except Exception as e:
        print("❌ Failed to post comment:", e)
