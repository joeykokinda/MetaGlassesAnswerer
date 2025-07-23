import os
from dotenv import load_dotenv

load_dotenv()


# put these below in an env if you plan on publicly sharing this project
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
LIVESTREAM_URL = os.getenv("LIVESTREAM_URL")

# Editable quiz behavior (can also move to .env if needed)
LIVESTREAM_REGION = (500, 150, 950, 1000)
DEFAULT_PROMPT = (
    "analyze quiz and output answers like: 1A; 2B; 3E. only respond with number and letter. "
    "if no quiz visible respond with 'cant see anything'"
)
CAPTURE_INTERVAL = 15
COOLDOWN_AFTER_REPEAT = 60
LOG_PATH = "logs/quiz_log.txt"
