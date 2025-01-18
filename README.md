# LiveAnswer

**LiveAnswer** is an automation tool that enhances real-time quiz answering during Instagram live streams. Designed for seamless integration with Meta Glasses, this bot uses **Selenium WebDriver**, **Pillow**, and the **OpenAI API** to automate login, navigation, screen capturing, quiz answering, and commenting in real-time.

---

## **How It Works**

1. **Two Accounts Setup**:
   - **Account 1**: Hosts the livestream. This account runs on your Meta Glasses, streaming the quiz.
   - **Account 2**: Watches the livestream. This account runs the `liveanswer.py` script to capture the quiz, analyze it, and post answers automatically.

2. **Automated Flow**:
   - Logs into Instagram using your credentials.
   - Navigates to the livestream URL.
   - Clicks once on the screen to start the livestream.
   - Captures screenshots of the livestream feed every 15 seconds after an initial 20-second delay.
   - Sends the screenshot to the OpenAI API to detect quiz questions and answers.
   - Posts the answers to the livestream as comments.

---

## **Features**

- **Automated Login**: Logs into Instagram with pre-configured credentials.
- **Quiz Answer Detection**: Processes livestream screenshots to extract quiz answers in the format `1A; 2B; 3C`.
- **Automated Commenting**: Posts extracted answers directly to the livestream comments.
- **Periodic Updates**: Captures and processes new images every 15 seconds.
- **Simple Screen Interaction**: Dismisses livestream overlays with a single click.

---

## **Prerequisites**

1. **Python Environment**:
   - Install Python 3.8+.
   - Install the required dependencies:
     ```bash
     pip install selenium pillow requests
     ```

2. **Google Chrome**:
   - Install Google Chrome.
   - Download and install [Chromedriver](https://chromedriver.chromium.org/downloads) matching your Chrome version.

3. **OpenAI API Key**:
   - Get your API key from [OpenAI](https://platform.openai.com/signup/).
   - Add it to the script in the `OPENAI_API_KEY` variable.

4. **Instagram Accounts**:
   - **Account 1**: Set up on your Meta Glasses to host the livestream.
   - **Account 2**: Used to run the script and post answers.

---

## **Configuration**

1. **Update Credentials**:
   - Replace placeholders in `liveanswer.py`:
     ```python
     INSTAGRAM_USERNAME = "your-email@example.com"
     INSTAGRAM_PASSWORD = "your-password"
     OPENAI_API_KEY = "your-openai-api-key"
     CHROMEDRIVER_PATH = "C:/path/to/chromedriver.exe"
     ```

2. **Adjust Livestream Region**:
   - Update the `livestream_region` in the script to match the screen coordinates of your livestream on your device:
     ```python
     livestream_region = (100, 100, 800, 1080)
     ```

---

## **Usage**

1. Start the livestream on **Account 1** (Meta Glasses).
2. Run the `liveanswer.py` script for **Account 2**:
   ```bash
   python liveanswer.py
