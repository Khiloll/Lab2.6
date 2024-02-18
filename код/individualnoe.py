#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Функция для добавления записи в список
def add_person(people_list):
    person = {}
    print("Введите данные о человеке:")
    person["фамилия"] = input("Фамилия: ")
    person["имя"] = input("Имя: ")
    person["знак Зодиака"] = input("Знак Зодиака: ")
    birthday = input("Дата рождения в формате дд.мм.гггг через точку: ").split('.')
    person["дата рождения"] = list(map(int, birthday))
    people_list.append(person)
    people_list.sort(key=lambda x: tuple(x["дата рождения"]))  # Сортировка по датам рождения
    print("Данные о человеке добавлены.")


# Функция для вывода информации о людях по знаку Зодиака
def display_people_by_zodiac(people_list, zodiac_sign):
    found = False
    print(f"Люди с знаком Зодиака '{zodiac_sign}':")
    for person in people_list:
        if person["знак Зодиака"] == zodiac_sign:
            print(f"{person['фамилия']} {person['имя']} - {person['дата рождения'][0]}.{person['дата рождения'][1]}.{person['дата рождения'][2]}")
            found = True
    if not found:
        print(f"Нет людей с знаком Зодиака '{zodiac_sign}'.")


# Список людей в виде словарей
people = []

# Добавление данных о людях
add_person(people)
add_person(people)

# Ввод знака Зодиака для поиска
search_zodiac = input("Введите знак Зодиака для поиска: ")
display_people_by_zodiac(people, search_zodiac)
