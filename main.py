import os
import time
import random
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

profile_path = f"{os.path.expanduser('~')}/?"

groups = [
    "@?",
    "@?",
    "@?",
    "@?",
    "@?",
    "@?",
    "@?",
    "@?",
    "@?",
    "@?",
]

message_text = """✨ JUPITER EXCHANGE AIRDROP IS NOW LIVE! ✨

💎 The cosmic rewards are finally here, and they’re 100% FREE for you to claim! 🎉 Don’t miss out on this incredible opportunity to receive exclusive tokens — no strings attached!

🚀 To get your hands on these FREE rewards, simply head over to the official Jupiter Exchange bot. It’s fast, easy, and completely hassle-free! Just follow the instructions and claim your tokens in no time.

🌍 With absolutely no cost and no hidden fees, you can dive into the world of DeFi with Jupiter Exchange. Whether you're a seasoned trader or a newbie, this airdrop is your gateway to the future of decentralized finance!

⭐️ Take advantage of this once-in-a-lifetime opportunity to be a part of the rapidly growing Jupiter Exchange ecosystem. Join the mission, claim your rewards, and step into the future of DeFi today!

🚀 The airdrop galaxy is waiting for you — claim your FREE tokens now through 👉 @❓❓❓ 👈 and embark on your journey to the stars! 🌟"""
    
def start_browser():
    options = Options()
    options.binary_location = "/usr/local/bin/firefox"
    options.add_argument("--headless")
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    options.set_preference("dom.webnotifications.enabled", False)
    options.set_preference("media.volume_scale", "0.0")
    options.add_argument(f"-profile")
    options.add_argument(profile_path)
    service = Service("/usr/local/bin/geckodriver")
    driver = webdriver.Firefox(service=service, options=options)
    driver.set_window_size(1280, 800)
    return driver

def main():
    driver = start_browser()
    driver.get("https://web.telegram.org/")
    time.sleep(50)

    for group in groups:
        try:
            url = f"https://web.telegram.org/k/#{group}"
            driver.get(url)
            print(f"Moved to {url}")
            time.sleep(20)

            message_input = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "div[contenteditable='true']")))

            driver.execute_script("arguments[0].scrollIntoView(true);",
                                  message_input)
            driver.execute_script("arguments[0].focus();", message_input)

            time.sleep(2)

            message_input.send_keys(f"{message_text} ({group})")
            message_input.send_keys(Keys.RETURN)
            print(f"Message sent to {group}")

            delay = random.randint(150, 300)
            print(f"Waiting {delay} sec...")
            time.sleep(delay)

        except Exception as e:
            print(f"Error in {group}: {e}")
            continue

    print("✅")
    driver.quit()


if __name__ == "__main__":
    main()
