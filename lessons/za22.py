# Миссия 1: Постройте бассейн кодом в майнкрафте
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()

# # Координаты, где будет располагаться бассейн
# x, y, z = mc.player.getTilePos()
# # Размеры бассейна
# width = 5
# length = 5
# depth = -4
# # Строим стены бассейна
# mc.setBlocks(x-1, y-1, z-1,
#              x + width+1, y + depth -1, z + length+1, 169)
# mc.setBlocks(x, y-1, z,
#              x + width, y + depth, z + length, 20)
# # Очищаем внутреннюю часть бассейна
# mc.setBlocks(x+1, y-1, z+1,
#              x + width - 1, y + depth + 1, z + length - 1, 0)
# # Заполняем пространство бассейна водой
# mc.setBlocks(x+1, y-1, z+1,
#              x + width -1, y + depth + 1, z + length -1, 10)

# Кортеж (tuple) - это структура данных в программировании, которая позволяет хранить несколько элементов различных типов внутри одного объекта. Кортежи являются неизменяемыми, то есть их элементы не могут быть изменены после создания кортежа. Кортежи обычно используются для группирования связанных данных внутри одного объекта.
# Кортежи очень похожи на списки, но имеют несколько отличий. Основное отличие состоит в том, что кортежи неизменяемы, в то время как списки могут быть изменены путем добавления, удаления или изменения элементов. Кортежи также обычно используются для хранения данных различных типов, в то время как списки часто содержат элементы одного типа.
# Кортежи могут быть созданы с помощью круглых скобок, например: (1, 2, 3) или ('apple', 'banana', 'orange'). Элементы внутри кортежа разделяются запятыми. Кортежи могут содержать любые типы данных, включая числа, строки, списки, другие кортежи и т. д.
# Для доступа к элементам кортежа используется индексация, как и в случае со списками. Например, чтобы получить доступ к первому элементу кортежа t, можно использовать выражение t[0].
# Пример использования кортежа в Python:
# Создание кортежа
# t = (1, 2, 3, 'apple')
# # Доступ к элементам кортежа
# print(t[0])  # Вывод: 1
# print(t[3])  # Вывод: 'apple'
# # Попытка изменить элемент кортежа вызовет ошибку
# t[0] = 5  # TypeError: 'tuple' object does not support item assignment

# # Что такое тип данных None
# result = None  # Присвоение переменной None
# print(result)  # Выводит: None
# print(type(result))  # Выводит: <class 'NoneType'>

# def process_data(data):
#     if data is None:
#         print("Нет данных")
#         return
    
#     # Обработка данных, если они доступны
#     print("Обработка данных:", data)

# # Вызов функции с None в качестве аргумента
# process_data(None)


# Миссия 2: Выведите типы данных
# Целочисленный тип данных
# integer_variable = 10
# print(type(integer_variable))

# # Вещественный тип данных
# float_variable = 3.14
# print(type(float_variable))

# # Комплексный тип данных
# complex_variable = 1 + 2j
# print(type(complex_variable))

# # Строковый тип данных
# string_variable = "Hello, World!"
# print(type(string_variable))

# # Логический тип данных
# bool_variable = True
# print(type(bool_variable))

# # Список (List)
# list_variable = [1, 2, 3]
# print(type(list_variable))

# # Кортеж (Tuple)
# tuple_variable = (4, 5, 6)
# print(type(tuple_variable))

# # Множество (Set)
# set_variable = {7, 8, 9}
# print(type(set_variable))

# # Словарь (Dictionary)
# dictionary_variable = {'key': 'value'}
# print(type(dictionary_variable))

# # None
# none_variable = None
# print(type(none_variable))

# Как работает одинарный массив + цикл фор
# my_array = [1, 2, 3, 4, 5]
# print(my_array[-1])

# # Итерация по элементам массива с помощью цикла "for"
# for element in my_array:
#     print(element)

# Как работает двойной массив + 2 цикла фор
# Определение двумерного массива (3x3 матрица)
# my_array = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10,11,12]
# ]
# print(my_array[3][2])
# Итерация по строкам матрицы с помощью первого цикла "for"
# for row in my_array:
#     # Итерация по столбцам внутри каждой строки с помощью второго цикла "for"
#     for element in row:
#         print(element)

# Как работает тройной массив + 3 цикла фор
# Определение трехмерного массива (3x3x3 куб)
# my_array = [
#     [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ],
#     [
#         [10, 11, 12],
#         [13, 14, 15],
#         [16, 17, 18]
#     ],
#     [
#         [19, 20, 21],
#         [22, 23, 24],
#         [25, 26, 27]
#     ]
# ]
# print(my_array[1][2][1])
# # # Итерация по высоте трехмерного массива с помощью первого цикла "for"
# for height in my_array:
#     # Итерация по строкам внутри каждого уровня высоты с помощью второго цикла "for"
#     for row in height:
#         # Итерация по столбцам внутри каждой строки с помощью третьего цикла "for"
#         for element in row:
#             print(element)

# Вы также можете использовать индексы высоты, ширины и глубины для доступа к элементам трехмерного массива внутри циклов "for". Вот пример:
# Определение трехмерного массива (3x3x3 куб)
# my_array = [
#     [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ],
#     [
#         [10, 11, 12],
#         [13, 14, 15],
#         [16, 17, 18]
#     ],
#     [
#         [19, 20, 21],
#         [22, 23, 24],
#         [25, 26, 27]
#     ]
# ]

# # # Итерация по индексам высоты с помощью первого цикла "for"
# for i in range(len(my_array)):
#     # Итерация по индексам строк внутри каждого уровня высоты с помощью второго цикла "for"
#     for j in range(len(my_array[i])):
#         # Итерация по индексам столбцов внутри каждой строки с помощью третьего цикла "for"
#         for k in range(len(my_array[i][j])):
#             print("Индекс высоты:", i, "Индекс строки:", j, "Индекс столбца:", k, "Значение:", my_array[i][j][k])

# # Как работает тройный массив с кортежами + 3 цикла фор
# # Определение трехмерного массива с кортежами (3x3x3 куб)
# my_array = [
#     [
#         [(1, 2), (3, 4,), (5, 6)],
#         [(7, 8), (9, 10), (11, 12)],
#         [(13, 14), (15, 16), (17, 18)]
#     ],
#     [
#         [(19), (20), (21), (22), (23), (24)],
#         [(25), (26), (27), (28), (29), (30)],
#         [(31), (32), (33), (34), (35), (36)]
#     ],
#     [
#         [(37, 38), (39, 40), (41, 42)],
#         [(43, 44), (45, 46), (47, 48)],
#         [(49, 50), (51, 52), (53, 54)]
#     ]
# ]
# print(my_array[1][0][0])
# # Итерация по высоте трехмерного массива с помощью первого цикла "for"
# for height in my_array:
#     # Итерация по строкам внутри каждого уровня высоты с помощью второго цикла "for"
#     for row in height:
#         # Итерация по столбцам внутри каждой строки с помощью третьего цикла "for"
#         for element in row:
#             print(element)

# Напишите функцию, которая принимает в себя массив и возвращает массив с числами которые делятся на два 
# def filter_even_numbers(arr):
#     result = []  # Создаем пустой массив для хранения чисел, делящихся на два
#     for num in arr:  # Итерируемся по каждому числу во входном массиве
#         if num % 2 == 0:  # Проверяем, делится ли число на два без остатка
#             result.append(num)  # Если число делится на два, добавляем его в результат
#     return result  # Возвращаем массив с числами, делящимися на два

# my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filtered_array = filter_even_numbers(my_array)
# print(filtered_array)  # Выводит: [2, 4, 6, 8, 10]


from tqdm import tqdm
# tqdm(...): Это функция из библиотеки tqdm, которая представляет собой простой прогресс-бар для отслеживания итераций в цикле. Она добавляет визуализацию прогресса выполнения цикла, что полезно для длительных операций, чтобы увидеть, сколько итераций уже завершено.

import keyboard
import time
import pickle
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def sortPair(val1, val2):
    if val1 > val2:
        return val2, val1
    else:
        return val1, val2


def copyStructure(x1, y1, z1, x2, y2, z2):

    x1, x2 = sortPair(x1, x2)
    y1, y2 = sortPair(y1, y2)
    z1, z2 = sortPair(z1, z2)

    width = x2 - x1
    height = y2 - y1
    length = z2 - z1

    sctructure = []
    print("Создание структуры...")

    for y in tqdm(range(height)):
        sctructure.append([])
        for z in range(length):
            sctructure[y].append([])
            for x in range(width):
                sctructure[y][z].append(mc.getBlockWithData(x1 + x, y1 + y, z1 + z))
    return sctructure


def buildScrtucture():
    while not keyboard.is_pressed('up'):
        print("Выберите первую точку")
        x1, y1, z1 = mc.player.getTilePos()
        time.sleep(1)
    while not keyboard.is_pressed('down'):
        print("Выберите вторую точку")
        x2, y2, z2 = mc.player.getTilePos()
        time.sleep(1)

    structure = copyStructure(x1+1, y1, z1+1, x2, y2, z2)

    while not keyboard.is_pressed('left'):
        print("Выберите точку для постройки")
        x, y, z = mc.player.getTilePos()
        time.sleep(1)
    print(f'\nx1,y1,z1: {x1, y1, z1}')
    print(f'x2,y2,z2: {x2, y2, z2}')

    yStart = y
    xStart = x+1
    zStart = z+1

    for y in tqdm(range(len(structure))):
        for z in range(len(structure[y])):
            for x in range(len(structure[y][z])):
                time.sleep(0.05)
                if structure[y][z][x].id != 0:
                    mc.setBlock(x + xStart, y + yStart, z + zStart, structure[y][z][x].id, structure[y][z][x].data)

buildScrtucture()