import pyautogui
import pyperclip
import time
from .credentials import get_credentials
from .browser_manage import BrowserManager

from .credentials import get_credentials

class Automation:
    def __init__(self):
        self.credentials = get_credentials()  # Получаем учетные данные

    def open_container_by_index(self, index):
        """Открывает контейнер по индексу, используя счетчик."""
        # Здесь указывайте комбинацию клавиш для открытия контейнера
        pyautogui.hotkey('ctrl', 'shift', str(index))  # Пример открытия нового окна
        time.sleep(1)  # Ждем, чтобы окно открылось


    def open_containers(self):
        """Открывает все контейнеры по списку учетных данных."""
        for index in range(len(self.credentials)):
            self.open_container_by_index(index)  # Открываем контейнер по индексу

        pyautogui.hotkey('alt','1')  # Если это первая вкладка
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'w')  # Закрываем первую вкладку
        time.sleep(1)
        
        pyautogui.hotkey('ctrl', 'l')  # Перейти в адресную строку
        pyautogui.copy("https://accounts.aliexpress.com/user/organization/manage_person_profile.htm?spm=a2g0o.account_setting")  # Вставляем URL
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        pyautogui.press('enter')  # Нажимаем Enter

