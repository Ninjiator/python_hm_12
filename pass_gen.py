import random
import string
import json

def generate_password(letters=True, symbols=False, numbers=False, duplicates=False, pass_length=8):
    # Довжина паролю не менше за 8 символів
    if pass_length < 8:
        print("Пароль має містити принаймні 8 символів")
        return

    charset = ""  # Рядок з символами для генерації паролю
    password = ""  # Змінна з генерованим паролем

    # Додавання символів в залежності від вказаних параметрів
    if letters:
        charset += string.ascii_letters  # Додаємо літери верхнього та нижнього регістру
    if symbols:
        charset += "!@#$%^&*()+"
    if numbers:
        charset += string.digits  # Додаємо цифри

    # Видаляємо повтори символів, якщо duplicates=False
    if not duplicates:
        charset = list(set(charset))

    # Якщо не було додано жодного символу, виводимо повідомлення та завершуємо функцію
    if len(charset) == 0:
        print("Немає символів для генерації паролю")
        return

    # Генерація паролю заданої довжини
    for i in range(pass_length):
        password += random.choice(charset)

    return password

def create_new_record():
    service = input("Введіть назву сервісу (наприклад, facebook, google, netflix): ")
    login = input("Введіть ваш логін: ")
    
    # Генеруємо пароль
    print("Введіть параметри для генерації пароля:")
    letters = input("Включити літери верхнього та нижнього регістру? (Так/Ні): ").lower() == 'так'
    symbols = input("Включити символи (!@#$%^&*()+)? (Так/Ні): ").lower() == 'так'
    numbers = input("Включити цифри? (Так/Ні): ").lower() == 'так'
    duplicates = input("Включити дублікати символів? (Так/Ні): ").lower() == 'так'
    pass_length = int(input("Введіть довжину пароля: "))

    password = generate_password(letters, symbols, numbers, duplicates, pass_length)

    # Записуємо дані в файл JSON
    record = {
        "title": service,
        "login": login,
        "password": password
    }
    with open("passwords.json", "a") as file:
        json.dump(record, file)
        file.write('\n')  # Додано перехід на новий рядок

    print("Запис успішно створено.")

def get_password_by_title():
    with open("passwords.json", "r") as file:
        records = file.readlines()

    service = input("Введіть назву сервісу для отримання паролю: ")
    for record in records:
        data = json.loads(record)
        if data["title"] == service:
            print("title:", data["title"])
            print("login:", data["login"])
            print("password:", data["password"])
            break
    else:
        print("Запис з такою назвою сервісу не знайдено.")

def main():
    while True:
        print("\nМеню:")
        print("1. Створити новий запис з паролем")
        print("2. Отримати пароль за полем title")
        print("3. Вийти")
        choice = input("Оберіть опцію: ")

        if choice == '1':
            create_new_record()
        elif choice == '2':
            get_password_by_title()
        elif choice == '3':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Будь ласка, виберіть знову.")

if __name__ == "__main__":
    main()
