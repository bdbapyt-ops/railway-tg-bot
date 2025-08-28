# Railway Telegram Bot 🚀

Python + [python-telegram-bot](https://python-telegram-bot.org) দিয়ে Railway-এ হোস্ট করা টেলিগ্রাম বট।

## 🚀 Deploy করার ধাপ

1. এই রিপো Fork/Clone করে নিজের GitHub-এ আপলোড করুন
2. Railway ড্যাশবোর্ডে যান → **New Project** → **Deploy from GitHub repo**
3. Deploy হয়ে গেলে → **Settings → Variables** এ গিয়ে `BOT_TOKEN` সেট করুন  
   (BotFather থেকে নেওয়া টোকেন)
4. Logs এ গেলে দেখবেন: `Bot is running...` ✅  
5. এখন টেলিগ্রামে গিয়ে `/start` লিখলে বট রেসপন্স করবে 🎉

---

## 🛠 প্রয়োজনীয় ফাইলসমূহ

- **bot.py** → মূল বট কোড
- **requirements.txt** → দরকারি পাইথন প্যাকেজ লিস্ট
- **Procfile** → Railway-কে বলে দেবে কীভাবে বট চালাতে হবে
- **README.md** → এই গাইডলাইন

---

## 📌 Example Commands

- `/start` → বট চালু হলে ওয়েলকাম মেসেজ দেবে  
- অন্য যেকোনো টেক্সট লিখলে → সেটার ইকো রিপ্লাই দেবে  

---

✍️ এখন তুমি GitHub এ কোড এডিট করলে Railway অটো ডিপ্লয় করে তোমার বট আপডেট করে দেবে।
