from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from selenium.webdriver.common.keys import Keys

options = webdriver.EdgeOptions()
prefs = {
    "profile.default_content_settings.popups": 0,
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

service = Service(r"C:\Users\opilane\source\repos\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=options)
wait = WebDriverWait(driver, 15)

try:
    # 1. Открываем сайт
    driver.get("https://quotes.toscrape.com")
    time.sleep(2)

    # 2. Вводим тег для поиска
    tag_input = driver.find_element(By.NAME, "tag")
    tag_input.send_keys("life")
    time.sleep(1)
    tag_input.send_keys(Keys.RETURN)
    time.sleep(2)

    # 3. Скроллим вниз и вверх
    driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    # 4. Открываем страницу логина в новой вкладке
    driver.execute_script("window.open('https://quotes.toscrape.com/login');")
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    # 5. Заполняем форму логина
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("my_test_user")
    time.sleep(1)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("123456")
    time.sleep(1)

    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    login_button.click()
    time.sleep(2)

finally:
    driver.quit()
