# MetaGlassesAnswerer 

MetaGlassesAnswerer is a Python automation tool that answers real-time quiz questions utlizing the Instagram live stream feature using Meta Glasses. It uses Selenium, Pillow, and OpenAI to capture livestream screenshots, extract questions and answers, and auto-comment responses—all without human interaction.

**Demo Video:**  
Watch it in action: [https://www.youtube.com/watch?v=eCDWHQe8cE0&t=1s](https://www.youtube.com/watch?v=eCDWHQe8cE0&t=1s)

---

## Features

- Automated Instagram login  
- AI-powered quiz answer detection via OpenAI API  
- uto-commenting extracted answers into the livestream  
- Periodic screenshotting every 15 seconds  
- Single-click interaction to dismiss overlays  
- Headless automation using Selenium + Pillow

---

## Getting Started

1. **Clone this repo**
   ```bash
   git clone https://github.com/joeykokinda/MetaGlassesAnswerer.git
   cd MetaGlassesAnswerer
   ```

2. **Install Python dependencies**
   ```bash
   pip install selenium pillow requests
   ```

3. **Install Google Chrome and ChromeDriver**
   - [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) matching your Chrome version.
   - Place it somewhere accessible and copy the path.

4. **Update credentials in `liveanswer.py`**
   ```python
   INSTAGRAM_USERNAME = "your-email@example.com"
   INSTAGRAM_PASSWORD = "your-password"
   OPENAI_API_KEY = "your-openai-api-key"
   CHROMEDRIVER_PATH = "C:/path/to/chromedriver.exe"
   livestream_region = (100, 100, 800, 1080)  # Adjust for your screen
   ```

5. **Start the livestream**
   - Account 1 (on Meta Glasses) should start the quiz livestream.
   - Account 2 runs the script and answers in real time.

6. **Run the bot**
   ```bash
   python liveanswer.py
   ```

---

## Example Output

**Input (Livestream Screenshot):**  
Point Your galsses at a multiple chocie quiz question
<img width="597" height="550" alt="image" src="https://github.com/user-attachments/assets/f09c3ad1-f0ec-49d1-929b-b9cd2b1cf799" />

**Output (Comments):**
```
1A  
2C  
3B  
```

---

## Security Notice

Use a throwaway or burner Instagram account. Do **not** use your personal credentials when automating login to third-party services. You can set up the livestream on your main account but the commenting one should be done with a burner.

---

## Future Ideas (If you would Like to make a pull request feel free to do so)

- Better input method, rather then taking screenshots at a certain time interval   
- Auto-region detection for livestream window
- Better way of sending photo (I have tried whatsapp and messagener but I have had no luck)

---

## License

MIT License — free to use, fork, and modify.

---

## Authors

- Joey Kokinda  
- Contributions welcome via pull requests
