import base64
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import ImageGrab

#path to chromedriver
CHROMEDRIVER_PATH = "path/to/your/chromedriver"

#api key
OPENAI_API_KEY = "your-api-key"

#login credentials
INSTAGRAM_USERNAME = "your-username"
INSTAGRAM_PASSWORD = "your-password"

#capture screen region
def capture_screen(region=None):
    try:
        if not region:
            region = (100, 100, 800, 1080)
        screenshot = ImageGrab.grab(bbox=region)
        screenshot.save("captured_image.jpg")
        return "captured_image.jpg"
    except Exception as e:
        print("error capturing screen:", e)
        raise

#encode image to base64
def encode_image_to_base64(image_path: str):
    try:
        with open(image_path, "rb") as image_file:
            base64_string = base64.b64encode(image_file.read()).decode("utf-8")
        return base64_string
    except Exception as e:
        print("error encoding image:", e)
        raise

#process image with api
def process_image_with_openai(image_base64: str):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    prompt = (
        "analyze quiz and output answers like: 1A; 2B; 3E. only respond with number and letter"
        "if no quiz visible respond with 'cant see anything'"
    )
    payload = {
        "model": "gpt-4-turbo",
        "messages": [
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}]
            },
        ],
        "max_tokens": 500,
    }
    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except requests.exceptions.RequestException as e:
        print("error processing image:", e)
        raise

#post comment to instagram
def post_comment_to_instagram(comment: str, driver):
    try:
        comment_box = driver.find_element(By.XPATH, "//textarea[@placeholder='Add a comment…']")
        comment_box.click()
        comment_box.send_keys(comment)
        time.sleep(1)
        comment_box.send_keys(Keys.RETURN)
        print("posted:", comment)
    except Exception as e:
        print("error posting comment:", e)

#login to instagram
def login_to_instagram(driver):
    try:
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        username_field.send_keys(INSTAGRAM_USERNAME)
        password_field.send_keys(INSTAGRAM_PASSWORD)
        
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)
        print("login successful")
    except Exception as e:
        print("error logging in:", e)
        raise

#click screen
def click_anywhere_on_screen(driver):
    try:
        driver.find_element(By.TAG_NAME, "body").click()
        print("clicked screen")
    except Exception as e:
        print("error clicking screen:", e)

#main loop
if __name__ == "__main__":
    try:
        service = Service(CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()

        login_to_instagram(driver)
        driver.get("https://www.instagram.com/your-target-account/live/")
        time.sleep(5)

        click_anywhere_on_screen(driver)
        print("starting bot")
        time.sleep(20)

        livestream_region = (500, 150, 950, 1000)

        while True:
            image_path = capture_screen(region=livestream_region)
            image_base64 = encode_image_to_base64(image_path)

            try:
                quiz_answers = process_image_with_openai(image_base64)
                if not quiz_answers or quiz_answers.lower() == "cant see anything":
                    print("no quiz found")
                else:
                    print("answers:", quiz_answers)
                    post_comment_to_instagram(quiz_answers, driver)
            except Exception as e:
                print("error:", e)

            time.sleep(15)

    except KeyboardInterrupt:
        print("bot stopped")
    except Exception as e:
        print("error:", e)
    finally:
        driver.quit()