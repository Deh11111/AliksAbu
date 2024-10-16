import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from browser_manage import AliExpressAutomation
import time 
# Функция для генерации случайного профиля
# def generate_random_profile():
#     profile_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
#     return profile_name

# # Создание случайного профиля
# profile_name = generate_random_profile()

# # Настройки для Firefox
# options = Options()
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

# # Запуск браузера Firefox с использованием случайного профиля
profile_path = "/home/sergey/.mozilla/firefox/ix82awpu.alik"
profile_browser = AliExpressAutomation(profile_path)


try:    
    # Переход по (ссылке)
    profile_browser.start_browser()
    profile_browser.driver.maximize_window()
    time.sleep(0.4)
    profile_browser.open_tabs_with_containers()
    time.sleep(3)
    
    profile_browser.open_url_aliexpress()
    time.sleep(1)
    profile_browser.open_google_login()
    # Нахождение и нажатие на элемент
    time.sleep(4)
    # google_element = profile_browser.driver.find_element(By.CSS_SELECTOR, ".fm-sns-new-item.google")
    # google_element = profile_browser.driver.find_element(By.XPATH, '//a[contains(@class, "fm-sns-new-item") and contains(@class, "google")]')

    
    # Дополнительный код для обработки после нажатия, если необходимо

finally:
    # Закрытие браузера
    print("GOOD")