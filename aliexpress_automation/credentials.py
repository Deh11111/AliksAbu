def get_credentials():
    """Чтение учетных данных из файла"""
    with open('credentials.txt', 'r') as file:
        credentials = file.read().splitlines()
    return credentials

