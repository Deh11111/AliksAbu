import time
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
        self.counts = 0

    def start_browser(self):
        # Запускает браузер с указанным профилем
        profile = FirefoxProfile(self.profile_path)
        options = Options()
        options.profile = profile

        # Запуск браузера с выбранным профилем
        self.driver = webdriver.Firefox(firefox_profile=profile)
        time.sleep(4)
       
    def read_credentials(self):
        """Читает данные из файла и сохраняет в переменные."""

        with open('credentials.txt', 'r') as file:
            line = file.readline().strip()  # Извлекаем первую строку
            self.email, self.password, self.reserve_email = line.split(':')
            print(f"Email: {self.email}, Password: {self.password}, Reserve Email: {self.reserve_email}")

        return count
    
    def open_url_aliexpress(self):

        # Нажатие на google_pic (замените на свою логику)
        counts = self.read_credentials()
        for i in range(1, counts):

            time.sleep(1)
            pyperclip.copy('https://accounts.aliexpress.com/user/organization/manage_person_profile.htm?spm=a2g0o.account_setting')
            
            time.sleep(0.5)
            pg.hotkey('ctrl', 'v')
            time.sleep(0.5)

            pg.hotkey('enter')
            print(i)
            time.sleep(2)
            pg.hotkey('ctrl', 'tab')


    def open_google_login(self): 

        pg.moveTo(x=731, y=600, duration=0.6)
        pg.leftClick(x=731, y=600)
        time.sleep(4) 

        # Копируем email в буфер обмена и вставляем
        pyperclip.copy(self.email)
        time.sleep(0.7)  # Ждем немного, чтобы система успела скопировать
        pg.hotkey('ctrl', 'v')  # Вставляем email
        
        time.sleep(1)  # Ждем, пока вставится email
        
        # Копируем пароль в буфер обмена и вставляем
        pyperclip.copy(self.password)
        time.sleep(0.7)  # Ждем немного, чтобы система успела скопировать
        pg.hotkey('ctrl', 'v')  # Вставляем пароль
        time.sleep(0.7)
        pg.hotkey('f6')
        time.sleep(0.3)
        pg.hotkey('ctrl','c')
        time.sleep(0.7)

        current_url = pyperclip.paste()
        if 'aliexpress' in current_url:
            print('Login Succesful')
        else:
            print(current_url)

        
    def close_browser(self):
        """Закрывает браузер."""
        if self.driver:
            self.driver.quit()

    def open_tabs_with_containers(self):
        """Открытие 10 вкладок с использованием контейнеров (Ctrl + Shift + 1-3)."""
        for i in range(1, count):  # Открываем контейнеры с 1 по index
            pg.hotkey('ctrl', 'shift', str(i))
            time.sleep(0.5)
        
        # Закрытие 1ой вкладки
        pg.hotkey('alt', '1')  # Переход на первую вкладку
        time.sleep(0.5) 
        pg.hotkey('ctrl', 'w') 
        
