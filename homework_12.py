import os
import string
from films_awards import films_awards  

films_titles = {
    "results": [
        {
            "imdb_id": "tt1201607",
            "title": "Harry Potter and the Deathly Hallows: Part 2"
        },
        {
            "imdb_id": "tt0241527",
            "title": "Harry Potter and the Sorcerer's Stone"
        },
        {
            "imdb_id": "tt0926084",
            "title": "Harry Potter and the Deathly Hallows: Part 1"
        },
        {
            "imdb_id": "tt0304141",
            "title": "Harry Potter and the Prisoner of Azkaban"
        },
        {
            "imdb_id": "tt0417741",
            "title": "Harry Potter and the Half-Blood Prince"
        },
        {
            "imdb_id": "tt0295297",
            "title": "Harry Potter and the Chamber of Secrets"
        },
        {
            "imdb_id": "tt0330373",
            "title": "Harry Potter and the Goblet of Fire"
        },
        {
            "imdb_id": "tt0373889",
            "title": "Harry Potter and the Order of the Phoenix"
        }
    ]
}

# Крок 1: Створення директорії "Harry Potter" та 8 піддиректорій
os.makedirs("Harry Potter", exist_ok=True)
for film in films_titles['results']:
    film_dir_name = film['title'].replace(":", "-").replace("/", "-")  # Заміна знаків, що неприйнятні для імен файлів
    film_dir = os.path.join("Harry Potter", film_dir_name)
    os.makedirs(film_dir, exist_ok=True)

# Крок 2: Створення піддиректорій від A до Z
for film in films_titles['results']:
    film_dir_name = film['title'].replace(":", "-").replace("/", "-")  # Заміна знаків, що неприйнятні для імен файлів
    film_dir = os.path.join("Harry Potter", film_dir_name)
    for letter in string.ascii_uppercase:
        letter_dir = os.path.join(film_dir, letter)
        os.makedirs(letter_dir, exist_ok=True)

# Крок 3: Створення списку нагород для кожного фільму
for film_awards in films_awards:
    film_title = film_awards['results'][0]['movie']['title']
    awards_list = []
    for award_info in film_awards['results']:
        award = {
            'type': award_info['type'],
            'award_name': award_info['award_name'],
            'award': award_info['award']
        }
        awards_list.append(award)
    # Крок 4: Відсортувати список нагород за алфавітом по ключу award_name
    sorted_awards_list = sorted(awards_list, key=lambda x: x['award_name'])
    # Крок 5-6: Створення та запис нагород у файли
    for award_info in sorted_awards_list:
        letter = award_info['award_name'][0]
        award_dir = os.path.join("Harry Potter", film_title.replace(":", "-").replace("/", "-"), letter)
        award_filename = os.path.join(award_dir, f"{award_info['award_name']}.txt")
        with open(award_filename, 'a', encoding='utf-8') as file:  # Вказуємо кодування UTF-8
            file.write(award_info['award'] + "\n")
