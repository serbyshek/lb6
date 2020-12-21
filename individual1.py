#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import sys

# Использовать словарь, содержащий следующие ключи: название товара; название
# магазина, в котором продается товар; стоимость товара в руб. Написать программу,
# выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из
# словарей заданной структуры; записи должны быть размещены в алфавитном порядке по
# названиям товаров; вывод на экран информации о товаре, название которого введено с клавиатуры;
# если таких товаров нет, выдать на дисплей соответствующее сообщение.

if __name__ == '__main__':
    products = []

    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break
        elif command == 'add':
            name = input("Название товара? ")
            shop = input("Название магазина? ")
            coast = int(input("Введите его цену "))
            product = {
                'name': name,
                'shop': shop,
                'coast': coast,
            }
            products.append(product)
            # Отсортировать список в алфавитном порядке
            if len(product) > 1:
                products.sort(key=lambda item: item.get('name', ''))
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
            )
            print(line)
            print(
                ' | {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    "№",
                    "Наименование товара",
                    "Название магазина",
                    "Стоимость"
                )
            )
            print(line)
            for idx, product in enumerate(products, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        idx,
                        product.get('name', ''),
                        product.get('shop', ''),
                        product.get('coast', 0)
                    )
                )
            print(line)
        elif command.startswith('select'):
            name_user = input("Введите название продукта ")

            count = 0
            for product in products:
                if name_user == product.get('name'):
                    count += 1
                    print(
                        '{:>4}: {} {} {}'.format(count, product.get('name', ' '), product.get('shop', ' '),
                        product.get('coast', ' '))
                    )
            if count == 0:
                print("Товар не найден")
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить товары;")
            print("list - вывести список товаров;")
            print("select - поиск товара")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)