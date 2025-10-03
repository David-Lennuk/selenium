from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

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

try:
    driver.get("https://www.tthk.ee/")
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, 300);")
    time.sleep(1)

    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    driver.refresh()
    time.sleep(1)

    driver.execute_script("window.open('https://httpbin.org/forms/post');")
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    name_input = driver.find_element(By.NAME, "custname")
    name_input.send_keys("Test")
    time.sleep(1)

    tel_input = driver.find_element(By.NAME, "custtel")
    tel_input.send_keys("123456789")
    time.sleep(1)

    driver.refresh()
    time.sleep(1)

    driver.get("https://davidlennuk23.thkit.ee/")
    time.sleep(2)
finally:
    driver.quit()
