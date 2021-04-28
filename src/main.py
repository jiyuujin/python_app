from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1280,1024")

driver = webdriver.Chrome(options=options)

driver.get("https://webneko.dev/")

time.sleep(3)

# docker-compose build
driver.save_screenshot("./data/screenshot.png")
