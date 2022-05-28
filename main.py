from random import randint
from json import dump

import faker

import conf


def main():
    """Основная функция, где творится дело"""
    with open("books.txt", mode='r', encoding='utf-8') as fn:
        names = fn.read()
    names = names.split()
    books = []
    if 'y' == input("Ввести pk 'y'? \n>"):
        pk = int(input("pk="))
        ge = gen(names, pk)
        for _ in range(conf.NUM_BOOKS):
            books.append(next(ge))
    else:
        ge = gen(names)
        for _ in range(conf.NUM_BOOKS):
            books.append(next(ge))
    with open("books.json", mode='w', encoding="utf-8") as f:
        dump(fp=f, obj=books, indent=4, ensure_ascii=False)


def gen(names: list, pk: int = 1) -> dict():
    """Наш любимый генератор книг"""
    while 1:
        book = dict()
        book["model"] = conf.MODEL
        book["pk"] = pk
        pk += 1
        fields = dict()
        fields["title"] = get_title(names)
        fields["year"] = get_year()
        fields["pages"] = get_pages()
        fields["isbn13"] = get_isbn13()
        fields["rating"] = get_rating()
        fields["price"] = get_price()
        fields["author"] = get_author()
        book["fields"] = fields
        yield book


def get_title(names: list) -> str:
    """Функция генерации имен, использует список книг, заранее полученных
     из books.txt"""
    return names[randint(0, 4)]


def get_year() -> int:
    """Функция генерации года издания, использует
     случайное число от 1600 до 2022"""
    return randint(1600, 2022)


def get_pages() -> int:
    """Функция генерации числа страниц книги, использует
     случайное число от 1 до 1200"""
    return randint(1, 1200)


def get_isbn13() -> str:
    """Функция генерации isbn13, использует модуль Faker для генерации
    случайного isbn13"""
    fak = faker.Faker(locale="ru-RU")
    return fak.isbn13()


def get_rating() -> float:
    """Функция генерации значения рейтинга книги, просто случайное число
     от 0 до 50, деленное на 10"""
    return randint(0, 50) / 10


def get_price() -> float:
    """Функция генерации цены книги, просто случайное число от 1 до 1000000,
     деленное на 10"""
    return randint(1, 10**6) / 10


def get_author() -> list:
    """Функция генерации имен автор(а/ов), сначала получаем число авторов
    случайное, а затем с помощью модуля Faker генерируем русские имена"""
    fak = faker.Faker(locale="ru-RU")
    count = randint(1, 3)
    authors = []
    for _ in range(count):
        authors.append(fak.name())
    return authors


if __name__ == "__main__":
    main()
