import csv
import json

# Відкриття файлу з даними про фільми
csv_file = open("films_data.csv", "r")
csv_list = csv.reader(csv_file)
dict_reader = csv.DictReader(csv_file)
films_dict = [row for row in dict_reader]

# Розділювач для виводу
separator = "-" * 40

def main():
    print("Програма пошуку інформації про фільми")
    print("Доступні команди: 'назва', 'жанр'")
    команда = input("Введіть команду: ").lower()
    if команда == 'назва':
        пошук_за_назвою()
    elif команда == 'жанр':
        пошук_за_жанром()
    else:
        print("Невірна команда. Будь ласка, спробуйте ще раз.")

def пошук_за_назвою():
    # Запит користувача на введення назви фільму
    назва_фільму = input("Введіть назву фільму: ").strip().casefold()
    # Пошук фільмів з введеною користувачем назвою
    знайдені_фільми = [film for film in films_dict if назва_фільму in film["title"].strip().casefold()]

    if not знайдені_фільми:
        print(separator, "Фільми не знайдено", sep="\n")
    elif len(знайдені_фільми) == 1:
        print(separator, "Інформація про фільм:\n", sep="\n")
        for film in знайдені_фільми:
            for key, value in film.items():
                print(f"\t{key}:\t{value}")
    else:
        вибір_фільму(знайдені_фільми)

def вибір_фільму(знайдені_фільми):
    print("Знайдено кілька фільмів:")
    for і, film in enumerate(знайдені_фільми, 1):
        print(f"{і}. {film['title']} ({film['year']})")

    # Вибір користувачем номера фільму
    while True:
        спроба = input("Виберіть номер фільму, щоб отримати детальну інформацію: ")
        try:
            номер_фільму = int(спроба)
            if 1 <= номер_фільму <= len(знайдені_фільми):
                break
            else:
                print("Невірний вибір. Будь ласка, введіть номер фільму зі списку.")
        except ValueError:
            print("Невірний ввід. Будь ласка, введіть номер фільму.")

    # Виведення інформації про обраний фільм
    обраний_фільм = знайдені_фільми[номер_фільму - 1]
    print(separator, "Інформація про фільм:\n", sep="\n")
    for key, value in обраний_фільм.items():
        print(f"\t{key}:\t{value}")

def пошук_за_жанром():
    # Створення словника з жанрами та списком фільмів для кожного жанру
    жанри = {}
    for film in films_dict:
        for genre in json.loads(film["gen"].replace("\'", "\"")):
            жанр = genre["genre"]
            if жанр in жанри:
                жанри[жанр].append(film["title"])
            else:
                жанри[жанр] = [film["title"]]

    # Виведення списку жанрів та кількості фільмів для кожного жанру
    print("Доступні жанри та кількість фільмів у кожному жанрі:")
    for жанр, фільми in жанри.items():
        print(f"{жанр}: {len(фільми)}")

    # Вибір користувачем жанру
    while True:
        спроба = input("Введіть номер жанру, щоб отримати список фільмів: ")
        try:
            номер_жанру = int(спроба)
            if 1 <= номер_жанру <= len(жанри):
                break
            else:
                print("Невірний вибір. Будь ласка, введіть номер жанру зі списку.")
        except ValueError:
            print("Невірний ввід. Будь ласка, введіть номер жанру.")

    # Виведення списку фільмів обраного жанру
    обраний_жанр = list(жанри.keys())[номер_жанру - 1]
    print(separator)
    print(f"Список фільмів у жанрі '{обраний_жанр}':")
    for фільм in жанри[обраний_жанр]:
        print(фільм)

if __name__ == '__main__':
    main()
