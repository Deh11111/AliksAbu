import time
import random
import pyperclip
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

class AliExpressAutomation:
    
    def __init__(self, profile_path):
        self.profile_path = profile_path
        self.driver = None
        self.email = ""
        self.password = ""
        self.reserve_email = ""

    def start_browser(self):
        # Настройки профиля
        profile = FirefoxProfile(self.profile_path)
        options = Options()
        
        # Задайте пользовательский агент
        options.set_preference("general.useragent.override", 
                               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36")
        
        # Запуск браузера с выбранным профилем
        self.driver = webdriver.Firefox(firefox_profile=profile, options=options)
        time.sleep(4)

    def read_credentials(self):
        """Читает данные из файла и сохраняет в переменные."""
        with open('credentials.txt', 'r') as file:
            line = file.readline().strip()  # Извлекаем первую строку
            self.email, self.password, self.reserve_email = line.split(':')
            print(f"Email: {self.email}, Password: {self.password}, Reserve Email: {self.reserve_email}")

    def open_url_aliexpress(self):
        """Копирует email и пароль в буфер обмена и вставляет их."""
        pyperclip.copy('https://accounts.aliexpress.com/user/organization/manage_person_profile.htm?spm=a2g0o.account_setting')
        
        time.sleep(random.uniform(1, 2))  # Случайная задержка
        pg.hotkey('ctrl', 'v')
        time.sleep(random.uniform(0.5, 1))  # Случайная задержка

        pg.hotkey('enter')
        time.sleep(random.uniform(2, 4))  # Случайная задержка

        self.read_credentials()
        # Копируем email в буфер обмена и вставляем
        pyperclip.copy(self.email)
        time.sleep(random.uniform(0.7, 1.5))  # Случайная задержка
        pg.hotkey('ctrl', 'v')  # Вставляем email
        
        time.sleep(random.uniform(1, 2))  # Случайная задержка
        
        # Копируем пароль в буфер обмена и вставляем
        pyperclip.copy(self.password)
        time.sleep(random.uniform(0.7, 1.5))  # Случайная задержка
        pg.hotkey('ctrl', 'v')  # Вставляем пароль
        time.sleep(random.uniform(0.7, 1.5))  # Случайная задержка
        
        pg.hotkey('f6')  # Переход к URL
        time.sleep(random.uniform(0.3, 1))  # Случайная задержка
        pg.hotkey('ctrl', 'c')  # Копирование URL
        time.sleep(random.uniform(0.7, 1.5))  # Случайная задержка

        current_url = pyperclip.paste()
        if 'aliexpress' in current_url:
            print('Login Successful')
        else:
            print(current_url)

    def close_browser(self):
        """Закрывает браузер."""
        if self.driver:
            self.driver.quit()

# Пример использования
profile_path = "/path/to/your/firefox/profile"
automation = AliExpressAutomation(profile_path)
automation.start_browser()
automation.open_url_aliexpress()
automation.close_browser()
