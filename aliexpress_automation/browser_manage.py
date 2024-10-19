from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from .selenium_profile import get_profile_settings
import time

class BrowserManager:
    
    def __init__(self, profile_path):
        self.profile_path = profile_path
    
    def create_firefox_profile(self):
        
        # Задает профилю настройки
        options = Options()
        options.profile = self.profile_path

        # Получаем настройки профиля из файла
        profile_settings = get_profile_settings()

        # Применяем настройки профиля
        for key, value in profile_settings.items():
            options.set_preference(key, value)

        # Создаем драйвер с настроенным профилем
        driver = webdriver.Firefox(service=FirefoxService(), options=options)
        time.sleep(2)
        return driver