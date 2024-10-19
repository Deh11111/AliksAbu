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

    def open_google_auth_url(self):   

        # Переход на страницу "Sign in with Google"
        pyautogui.hotkey('ctrl', 'l')  # Перейти в адресную строку
        time.sleep(1)
        pyperclip.copy("https://accounts.google.com/v3/signin/identifier?opparams=%253F&dsh=S-1254757662%3A1729134609358951&client_id=438567566819-3k1nk9qd1vr39c42rmjr0dh24ngth0s4.apps.googleusercontent.com&ddm=0&o2v=2&redirect_uri=https%3A%2F%2Fthirdparty.aliexpress.com%2Fggcallback.htm&response_type=code&scope=openid+email+profile&service=lso&state=PVypwA%2FdbXlMo31bU3h0G44dfivWfrY6o%2F5mRUfWUlXX1vLSDDrMWDvxs%2BHFzbel34SeQtYlzzOlw8%2FXONLrp8d3nAtyRUq7w3%2FjJNwAUtwyJ9LhwTzi6%2FFoN3bABMplymDR%2BFXpx44%2F1D6eMRPR%2Bm6GLkohJt6xVpSl6TXjsbXposiNWxoplqp7hDaraBfCUVKnXT9Vv6w5uJLLyZaIRQ%3D%3D&flowName=GeneralOAuthFlow&continue=https%3A%2F%2Faccounts.google.com%2Fsignin%2Foauth%2Fconsent%3Fauthuser%3Dunknown%26part%3DAJi8hAPpD6bW96bGwSgECk5ZQPJNvqD4K2CPcOHdaRWmUiXxOOYk0IY8dQjx260Wq0C6mW1e7a8CIkWLHkJrLaemTso3PH8EuB6GTaTCSBeJ8rdMmY9K42IBmlU0Rn7RkILPW1xLDNOMmCXSVJxb9p32QLkVzoRXr942YDUbRkEsoQ41VHED6ae7x-QJkeJ3W4T96YuXHEBBCjPVt4GMhDxgGae8RE8Ak0qG2ezfLzOOh2IrTPkYZkKo0nFZlGBfZAY1Z-nE07w7GS6_msPr5fnmMJczIMoJluM_L86mKaofgWbreM6sDdM0tvdFllpLmbXMSaeA-kQG9WHgk0yXym2FXsRzyVeJUGDR_JriIHs51kcbvvejtRETypHtuNwXXfAdyhEVMv4IABL0OEs2gPfKy-CvrE38p3uJcmAH2o4736ZmUwYWrzSKZVIcA1XfaUsMUzuAox5NDOWHgfAFiWYQsG3-cd8nLfuq28ko4hX2b3rS__LEVz4%26flowName%3DGeneralOAuthFlow%26as%3DS-1254757662%253A1729134609358951%26client_id%3D438567566819-3k1nk9qd1vr39c42rmjr0dh24ngth0s4.apps.googleusercontent.com%23&app_domain=https%3A%2F%2Fthirdparty.aliexpress.com&rart=ANgoxcfg35yPdktUnlnFkdz2e_qfZM4omICaJFMfzVjaLfxKDx4c4AVqHGEXKAXeULuJ2ORWL19TfklwlMz1b8g80Barq8yM9CeZ6CV0SoQ4BYr-vxI7TWw")  # Вставляем URL
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        pyautogui.press('enter')  # Нажимаем Enter
        time.sleep(3)


    # def check_status_sign_page(self):

    #     # Проверка не зажевало ли о фроде 
    #     pyautogui.hotkey('ctrl', 'l')
    #     time.sleep(1)
    #     pyautogui.hotkey('ctrl', 'с')
    #     time.sleep(1)
    #     buffer_text = pyperclip.paste()
    #     time.sleep(0.5)

    #     if "captcha" in buffer_text:
    #         print("PIZDA CAPTCHA. No INKOGNITO")


    # def switch_container_by_index(self, index):
        # pyautogui.hotkey('alt', str(index))