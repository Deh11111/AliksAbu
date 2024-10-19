from aliexpress_automation.automation import Automation

browser = Automation()

if __name__ == "__main__":
    # Запуск основной логики автоматизации
    print("Автоматизация запущена")
    browser.open_containers()
    browser.open_url()
    print("Автоматизация завершена")