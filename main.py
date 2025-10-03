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
    # 1. Открываем сайт example.com
    driver.get("https://example.com")
    time.sleep(2)

    # 2. Скроллим немного вниз
    driver.execute_script("window.scrollTo(0, 300);")
    time.sleep(1)

    # 3. Скроллим обратно вверх
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    # 4. Обновляем страницу
    driver.refresh()
    time.sleep(1)

    # 5. Открываем вторую вкладку с формой
    driver.execute_script("window.open('https://httpbin.org/forms/post');")
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    # 6. Вводим имя
    name_input = driver.find_element(By.NAME, "custname")
    name_input.send_keys("Test")
    time.sleep(1)

    # 7. Вводим телефон
    tel_input = driver.find_element(By.NAME, "custtel")
    tel_input.send_keys("123456789")
    time.sleep(1)

    # 8. Скроллим немного вниз по форме
    driver.execute_script("window.scrollTo(0, 300);")
    time.sleep(1)

    # 9. Скроллим обратно вверх по форме
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    # 10. Нажимаем кнопку отправки формы
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    time.sleep(2)

finally:
    driver.quit()
