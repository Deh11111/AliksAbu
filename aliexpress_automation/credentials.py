class AccountManager:

    def __init__(self, filename='/home/sergey/Desktop/ALIK_SCR/Alex_login_clcker/credentials.txt'):
        self.filename = filename
        self.credentials = self.load_credentials()

    def load_credentials(self):
        # Чтение учетных данных из файла
        credentials_dict = {}
        with open(self.filename, 'r') as file:
            lines = file.read().splitlines()
            # Начинаем индексацию с 1
            for idx, line in enumerate(lines, start=1):
                # Разбиваем строку на email, pass, reserve_email
                email, password, reserve_email = line.split(':')
                # Сохраняем данные в словарь с индексом начиная с 1
                credentials_dict[idx] = {
                    'email': email,
                    'password': password,
                    'reserve_email': reserve_email
                }
                
        return credentials_dict

    def get_credentials(self, index):
        # Получаем данные по индексу
        return self.credentials.get(index, None)

# Пример использования:
manager = AccountManager()
print(manager.get_credentials(1))  # Теперь выводит данные для первого аккаунта
print(manager.get_credentials(2))  # Данные для второго аккаунта
