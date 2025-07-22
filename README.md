# MetaGlassesAnswerer 🎯

MetaGlassesAnswerer is a Python automation tool that answers real-time quiz questions during Instagram live streams using Meta Glasses. It uses Selenium, Pillow, and OpenAI to capture livestream screenshots, extract questions and answers, and auto-comment responses—all without human interaction.

🎥 **Demo Video:**  
Watch it in action: [https://www.youtube.com/watch?v=eCDWHQe8cE0&t=1s](https://www.youtube.com/watch?v=eCDWHQe8cE0&t=1s)

---

## 🛠 Features

- 🔐 Automated Instagram login  
- 🧠 AI-powered quiz answer detection via OpenAI API  
- 💬 Auto-commenting extracted answers into the livestream  
- 🔄 Periodic screenshotting every 15 seconds  
- 🖱️ Single-click interaction to dismiss overlays  
- 🧪 Headless automation using Selenium + Pillow

---

## 🚀 Getting Started

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

## 🖼 Example Output

**Input (Livestream Screenshot):**  
*Sample image here if you have one*

**Output (Comments):**
```
1A  
2C  
3B  
```

---

## ⚠️ Security Notice

Use a throwaway or burner Instagram account. Do **not** use your personal credentials when automating login to third-party services.

---

## ✅ TODO / Future Ideas

- OCR tuning for blurry quiz feeds  
- Add Twitch/YouTube livestream support  
- Overlay viewer for real-time answer display  
- Auto-region detection for livestream window  

---

## 📄 License

MIT License — free to use, fork, and modify.

---

## 👥 Authors

- Joey Kokinda  
- Contributions welcome via pull requests
