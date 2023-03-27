from tabulate import tabulate
import variable
import sys, os
clear = lambda: os.system('cls')


def print_menu():
    print(f'''\nГлавное меню:
    1. Показать контакты
    2. Создать контакт
    3. Найти контакт
    4. Изменить контакт
    5. Удалить контакт
    6. Выход
    \n{variable.menu_selection}''', end='')
    while True:
        try:
            user_input = int(input())
            if 0 < user_input < 7:
                return user_input
            else:
                print(variable.error)
        except:
            print(variable.error)

# print_msg(msg): функция для вывода сообщения на экран пользователя
# def print_msg(msg):
#     print(50 * "_")
#     print(msg)
#     print(50 * "_")

# print_phonebook(): функция для вывода справочника
def print_phonebook(arr):
    clear()
    print('\n', variable.open_book)
    print(tabulate(arr, headers=variable.first_line))