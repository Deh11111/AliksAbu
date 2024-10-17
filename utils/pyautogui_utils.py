import pyautogui as pg
import time

def move_and_click(x, y, duration=0.6):
    """Перемещает курсор и нажимает на координаты"""
    pg.moveTo(x, y, duration=duration)
    pg.click()
    time.sleep(1)  # Задержка после клика

def open_tabs(count):
    for i in range(count):
        pg.hotkey('ctrl', 'shift', str(i + 1))  # Открыть контейнер
        pg.hotkey('ctrl', 't')  # Открыть новую вкладку
        pg.sleep(1)  # Пауза для загрузки вкладки