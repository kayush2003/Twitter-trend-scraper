import time
import uuid
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pymongo import MongoClient
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# MongoDB Setup
client = MongoClient("mongodb://localhost:27017/")
db = client["twitter_trends"]
collection = db["trending_topics"]

# ProxyMesh Setup
PROXY_URL = "http://ayush50:43s!&nS@r~e$@_6@us-ca.proxymesh.com:31280"

def get_trending_topics():
    unique_id = str(uuid.uuid4())
    chrome_options = Options()
    # chrome_options.add_argument(f"--proxy-server={PROXY_URL}")

    # Selenium WebDriver
    driver = webdriver.Chrome(service=Service(r"C:\Users\Lenovo\Downloads\chromedriver-win64\chromedriver.exe"), options=chrome_options)

    try:
        driver.get("https://twitter.com/login")

        # Wait for the username field to be present
        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        username.send_keys("AyushKu59663560")
        
        # Wait and click the "Next" button
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))
        )
        next_button.click()

        # Wait for the password field
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password.send_keys("maa@7352")

        # Wait and click the "Log in" button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Log in']"))
        )
        login_button.click()

        # Wait for the home page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-testid='primaryColumn']"))
        )

        # Fetch trending topics
        driver.get("https://twitter.com/home")
        time.sleep(5)  # Small delay to ensure content loads

        trends = driver.find_elements(By.XPATH, "//div[@data-testid='trend']")
        top_trends = [trend.text for trend in trends[:5]]

        # Get IP address (simulated as platform information)
        ip_address = driver.execute_script("return window.navigator.platform;")
        end_time = datetime.now()

        # Save to MongoDB
        record = {
            "_id": unique_id,
            "trend1": top_trends[0] if len(top_trends) > 0 else None,
            "trend2": top_trends[1] if len(top_trends) > 1 else None,
            "trend3": top_trends[2] if len(top_trends) > 2 else None,
            "trend4": top_trends[3] if len(top_trends) > 3 else None,
            "trend5": top_trends[4] if len(top_trends) > 4 else None,
            "end_time": end_time.strftime("%Y-%m-%d %H:%M:%S"),
            "ip_address": ip_address,
        }

        collection.insert_one(record)
        driver.quit()
        return record

    except Exception as e:
        driver.quit()
        print(f"Error occurred: {e}")
        raise e

if __name__ == "__main__":
    try:
        result = get_trending_topics()
        print("Scraping completed. Result:")
        print(result)
    except Exception as e:
        print(f"Scraping failed: {e}")
