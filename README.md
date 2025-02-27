# LinkedIn Auto-Unfollow Bot (2025)

Automate **mass unfollowing** of LinkedIn connections using Selenium and Python. This script helps you **unfollow all connections** without manually clicking through your LinkedIn network.

## 🚀 Features
- **Automates Unfollowing**: Unfollows all connections on LinkedIn.
- **Uses Your Existing Chrome Session**: No need to log in manually.
- **Avoids LinkedIn Security Blocks**: Runs inside your real Chrome profile.
- **Scrolls Automatically**: Loads more connections while unfollowing.

---

## 📌 Installation & Setup

### **1️⃣ Install Python & Dependencies**
Make sure you have **Python 3.7+** installed.

#### **Install Required Packages**
```sh
pip install selenium webdriver-manager
```

### **2️⃣ Find Your Chrome Profile Path**
1. Open **Google Chrome**.
2. In the address bar, type:
   ```
   chrome://version/
   ```
3. Look for **"Profile Path"**, which looks like:
   ```
   C:\Users\YourUsername\AppData\Local\Google\Chrome\User Data\Default
   ```
4. Copy this path for the next step.

---

## 📜 Script: `linkedin_unfollow.py`

Create a Python script (`linkedin_unfollow.py`) and **replace `YOUR_PROFILE_PATH`** with your actual Chrome profile path.

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# ✅ Use an existing Chrome profile (Replace this with your actual path)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(r"user-data-dir=C:\Users\YourUsername\AppData\Local\Google\Chrome\User Data")
chrome_options.add_argument(r"profile-directory=Default")  # Change if using multiple profiles
chrome_options.add_argument("--disable-webrtc")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# ✅ Start Chrome with your existing session
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# ✅ Go to LinkedIn "Following" page
driver.get("https://www.linkedin.com/mynetwork/network-manager/")

time.sleep(5)  # Wait for page to load

# ✅ Unfollow loop
while True:
    try:
        # Find all "Following" buttons
        unfollow_buttons = driver.find_elements(By.XPATH, "//button[contains(., 'Following')]")

        if not unfollow_buttons:
            print("✅ Unfollow complete. No more connections to unfollow.")
            break

        for btn in unfollow_buttons:
            driver.execute_script("arguments[0].click();", btn)
            time.sleep(2)  # Avoid rate limits

        # Scroll down to load more
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(3)

    except Exception as e:
        print(f"⚠️ Error: {e}")
        break

driver.quit()
print("✅ All connections unfollowed!")
```

---

## 🎯 Running the Script
1. **Modify the script**:
   - Replace `YOUR_PROFILE_PATH` with your actual Chrome profile path.
2. **Run the script**:
   ```sh
   python linkedin_unfollow.py
   ```
3. **LinkedIn will open**, and the script will start unfollowing!

---

## 🛠 Troubleshooting
### **1️⃣ 'chrome.exe' Not Found?**
- Make sure Google Chrome is installed and added to your system’s PATH.

### **2️⃣ Selenium Session Errors?**
- Close any **open Chrome instances** before running the script.
- Delete **old session data** and restart:
  ```sh
  rmdir /S /Q "C:\Users\YourUsername\AppData\Local\Google\Chrome\User Data\Default"
  ```

### **3️⃣ LinkedIn Blocks Automation?**
- Use a **VPN or different network** to avoid detection.
- **Reduce speed** by increasing `time.sleep()` in the script.

---

## ⚠️ Disclaimer
This tool is for **educational purposes only**. Automating LinkedIn actions may **violate LinkedIn’s Terms of Service**. Use it responsibly!

---

## 📢 Contribution & Feedback
- Found a bug? **Submit an issue**.
- Want a feature? **Create a pull request**.
- Love the tool? **Give it a ⭐ on GitHub!**

Happy Unfollowing! 🚀

