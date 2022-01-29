__author__ = 'Болотов Андрей Вячеславович'
"""
6. Реализовать структуру данных «Товары». 
Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. 
В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара: 
название, цена, количество, единица измерения. 
Структуру нужно сформировать программно, запросив все данные у пользователя.
Пример готовой структуры:

[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Нужно собрать аналитику о товарах. 
Реализовать словарь, в котором каждый ключ — характеристика товара, например, название. 
Тогда значение — список значений-характеристик, например, список названий товаров.
Пример:

{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""


def products_input(numbers, specifications):
    """
    Заполняет характеристики товара
    :param numbers: целое положительное цисло
    :param specifications: список характеристик
    :return: список кортежей с двумя элиментами : номер товара и словарь с параметрами
    """
    products = []
    products_dict = {}
    """
    Сделал такую структуру что бы преобразовать в число строку если она состоит толко из цифр
    Если не надо преобразовывать то можно сдетать проще
    for i in range(1, number + 1):
        products.append((i,{key: input(f'Введите {key} продукта : ') for key in specifications})
    """
    for i in range(1, numbers + 1):
        for key in specifications:
            el = input(f'Введите {key} {i}-го продукта : ')
            product_dict = {key: int(el) if el.isdigit() else el}
            products_dict.update(product_dict)
        products.append((i, products_dict))
    return products


def analytics_products(specifications, products):
    """
    Формирует словарь для аналитики
    :param specifications: список характеристик
    :param products: список продуктов
    :return: словарь где ключ - характеристика товара, а значение - список значений-характеристик
    """
    analytics = {}
    for item in specifications:
        my_list = []
        for i in range(len(products)):
            my_list.extend(value for key, value in products[i][1].items() if key == item)
        my_dict = {item: my_list}
        analytics.update(my_dict)
    return analytics


specifications_product = ["название", "цена", "количество", "eд"]
number_products = input('Введите количество товара, которого хотите ввести : ')
while not number_products.isdigit():
    number_products = input('Это должно быть число!\n')
    if number_products < 0:
        print('Число должно быть болше нуля!\n')
        number_products = " "
products = products_input(number_products, specifications_product)
analytics = analytics_products(specifications_product, products)
print(*products, sep="\n")
print(analytics)
