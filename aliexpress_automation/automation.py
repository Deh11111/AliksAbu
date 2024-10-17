import pyautogui
import pyperclip
import time
from .credentials import AccountManager
from .browser_manage import BrowserManager

# Инициализируем объект класса AccountManager
manager = AccountManager()

class Automation:
    def __init__(self):
        self.credentials = manager.get_credentials()  # Получаем учетные данные

    def open_container_by_index(self, index):

        # Открывает контейнер по индексу, используя счетчик.
        # Здесь указывайте комбинацию клавиш для открытия контейнера
        pyautogui.hotkey('ctrl', 'shift', str(index))  # Пример открытия нового окна
        time.sleep(1)  # Ждем, чтобы окно открылось

    def open_containers(self):

        # Открывает все контейнеры по списку учетных данных
        for index in range(len(self.credentials)):
            self.open_container_by_index(index)  # Открываем контейнер по индексу
            time.sleep(1)
            self.open_url() # Открываем ссылку

        pyautogui.hotkey('alt','1')  # Если это первая вкладка
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'w')  # Закрываем первую вкладку
        time.sleep(1)
        print("Containers OPENED!")

    def open_url(self):   

        # Переход на страницу "Sign in with Google"
        pyautogui.hotkey('ctrl', 'l')  # Перейти в адресную строку
        time.sleep(1)
        pyperclip.copy("https://accounts.aliexpress.com/user/organization/manage_person_profile.htm?spm=a2g0o.account_setting")  # Вставляем URL
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        pyautogui.press('enter')  # Нажимаем Enter

    def open_login_google(self):

        self.open_containers()
        time.sleep(0.5)
        self.open_url()

    def check_status_sign_page(self):

        # Проверка не зажевало ли о фроде 
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'с')
        time.sleep(1)
        buffer_text = pyperclip.paste()
        time.sleep(0.5)

        if "captcha" in buffer_text:
            print("PIZDA CAPTCHA. No INKOGNITO")

            
    # def switch_container_by_index(self, index):
        # pyautogui.hotkey('alt', str(index))