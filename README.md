# MetaGlassesAnswerer

MetaGlassesAnswerer is a Python automation tool that answers real-time quiz questions utilizing the Instagram live stream feature using Meta Glasses. It uses Selenium, Pillow, and OpenAI to capture livestream screenshots, extract questions and answers, and auto-comment responses—all without human interaction.

**Demo Video:**  
Watch it in action: [https://www.youtube.com/watch?v=eCDWHQe8cE0&t=1s](https://www.youtube.com/watch?v=eCDWHQe8cE0&t=1s)

---

## Features

- Automated Instagram login  
- AI-powered quiz answer detection via OpenAI API  
- Auto-commenting extracted answers into the livestream  
- Periodic screenshotting every 15 seconds (configurable)  
- Single-click interaction to dismiss overlays  
- Modular structure with environment variable configuration  
- Automatic answer logging with timestamps

---

## Getting Started

1. **Clone this repo**
   ```bash
   git clone https://github.com/joeykokinda/MetaGlassesAnswerer.git
   cd MetaGlassesAnswerer
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Google Chrome and ChromeDriver**
   - [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) matching your Chrome version.
   - Place it somewhere accessible and copy the path.

4. **Create a `.env` file in the project root**

   Add the following values:
   ```
   CHROMEDRIVER_PATH=C:/path/to/chromedriver.exe
   OPENAI_API_KEY=your-openai-api-key
   INSTAGRAM_USERNAME=your-burner-username
   INSTAGRAM_PASSWORD=your-password
   LIVESTREAM_URL=https://www.instagram.com/targetaccount/live/
   ```

5. **Start the livestream**
   - Account 1 (on Meta Glasses or phone) should start the quiz livestream.  
     This can be your main account or a burner.
   - Account 2 (the one listed in the `.env` file) runs the script and auto-answers in real time.

6. **Run the bot**
   ```bash
   python main.py
   ```

   To override the prompt:
   ```bash
   python main.py --prompt "only respond with the correct letter like: 1A; 2C"
   ```

---

## Example Output

**Input (Livestream Screenshot):**  
Point your glasses at a multiple choice quiz question.
<img width="597" height="550" alt="image" src="https://github.com/user-attachments/assets/f09c3ad1-f0ec-49d1-929b-b9cd2b1cf799" />

**Output (Comments):**
```
1A  
2C  
3B  
```

---

## Security Notice

Use a burner Instagram account for automation. Do not use your personal credentials in this tool. The livestream can be hosted from your main account, but the account logging in to comment should be a throwaway.

---

## Logging

Answers are automatically saved to `logs/quiz_log.txt` with timestamps. This helps track quiz performance or debug the output later.

---

## Future Ideas (Pull Requests Welcome)

- Smarter input triggers (e.g., detect when a quiz actually changes)  
- Auto-region detection for livestream window  
- Alternate image input methods (attempts via WhatsApp/Messenger were unsuccessful so far)  
- Simple UI or config form for non-technical users

---

## License

MIT License — free to use, fork, and modify.

---

## Authors

- Joey Kokinda  
- Contributions welcome via pull requests
