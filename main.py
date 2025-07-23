# main.py

import time
import argparse
from functions import (
    CHROMEDRIVER_PATH, LIVESTREAM_URL, LIVESTREAM_REGION,
    DEFAULT_PROMPT, CAPTURE_INTERVAL, COOLDOWN_AFTER_REPEAT
)
from functions import init_driver, login, start_livestream, post_comment
from functions import capture_screen
from utils import read_image_as_base64, log_quiz_result
from functions import process_image_with_openai

def main(prompt_override=None):
    prompt = prompt_override if prompt_override else DEFAULT_PROMPT
    last_answer = ""
    last_time = 0

    driver = init_driver(CHROMEDRIVER_PATH)

    try:
        login(driver)
        start_livestream(driver, LIVESTREAM_URL)

        while True:
            image_path = capture_screen(region=LIVESTREAM_REGION)
            image_b64 = read_image_as_base64(image_path)
            answer = process_image_with_openai(image_b64, prompt)

            now = time.time()
            if answer.lower() == "cant see anything":
                print("No quiz found.")
            elif answer == last_answer and now - last_time < COOLDOWN_AFTER_REPEAT:
                print("Duplicate answer skipped.")
            else:
                post_comment(driver, answer)
                log_quiz_result(answer)
                last_answer = answer
                last_time = now

            time.sleep(CAPTURE_INTERVAL)

    except KeyboardInterrupt:
        print("Bot stopped")
    finally:
        driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", help="Custom OpenAI prompt")
    args = parser.parse_args()

    main(prompt_override=args.prompt)
