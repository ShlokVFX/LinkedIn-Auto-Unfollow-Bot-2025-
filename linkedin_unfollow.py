from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# ✅ Use an existing Chrome profile (change this to your profile path)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(r"user-data-dir=C:\Users\elect\AppData\Local\Google\Chrome\User Data") # replace with your own path
chrome_options.add_argument(r"profile-directory=Default")  # Change if you use multiple profiles
chrome_options.add_argument("--disable-webrtc")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# ✅ Start Chrome with your existing session
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# ✅ Go to "Following" page (no login required since profile is already logged in)
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
