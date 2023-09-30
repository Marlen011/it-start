# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# def square(x_b, y_b, z_b, block):
#     x,y,z = mc.player.getPos()
#     mc.setBlocks(x,y,z,
#                  x+x_b, y+y_b, z+z_b, block)
# square(4,4,4,47)

# my_list = [1,2,3.0,'four',True,[4,77,42]] # mis1
# print(my_list[-1][1])

# for i in my_list:
#     print(i)

# count_o = len(my_list)
# for i in range(count_o):
#     my_list[i] = input('enter new list: ')
#     # print(my_list[i])
# print(my_list)

# mis1
# print(my_list)

# mis2
# my_list = [[1,2,3,], [4,5,6], [7,8,9]]
# print(my_list[0][0])

# mis3
# my_list = [1,2,[3,4,'atmosphere',6,'seven'], 'Marlen',[9,'uwu','zzz']]
# print(my_list[-1][1])

# На самом деле айди блока в майнкрафте сложнее чем кажется
# Рассказать getBlockWithData
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# x,y,z = mc.player.getTilePos()
# block = mc.getBlockWithData(x,y+2,z)
# pos = str(x) + ' ' + str(y) + ' ' + str(z)
# block_id = block.id
# block_data = block.data
# print(f"Блок на координатах: {pos}")
# print(f"ID блока: {block_id}")
# print(f"Дополнительные данные блока: {block_data}")

# Миссия: Поставить блок и получить его айди
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# x,y,z=mc.player.getTilePos()
# block_move = 2
# block_id = 47
# mc.setBlock(x+block_move,y,z,block_id)
# print(f'block\'s id on position ({x+block_move}, {y}, {z}): {block_id}')

""" Кортеж (tuple), массив (array) и список (list) в Python являются разными типами данных и имеют различные свойства и функциональность.
Кортеж (tuple):
Упорядоченная и неизменяемая коллекция элементов.
Элементы хранятся в порядке, и доступ к ним осуществляется по индексу.
Создается с использованием круглых скобок () или функции tuple().
Пример: my_tuple = (1, 2, 3)

Массив (array):
Одномерный, упорядоченный и изменяемый набор элементов одного типа.
Элементы массива имеют фиксированный тип данных.
Обычно используется в модуле array для эффективного хранения и манипуляций с числовыми данными.
Создается с использованием функции array() из модуля array.
Пример: import array; my_array = array.array('i', [1, 2, 3])

Список (list):
Упорядоченная и изменяемая коллекция элементов разных типов.
Элементы списка могут быть изменены, добавлены или удалены.
Создается с использованием квадратных скобок [] или функции list().
Пример: my_list = [1, 'two', 3.0]
Основное различие между кортежами и списками заключается в том, что кортежи являются неизменяемыми, в то время как списки могут быть изменены. Массивы, с другой стороны, предоставляют специализированные возможности для эффективной работы с числовыми данными.
Каждый из этих типов данных имеет свои особенности и применение в различных ситуациях, и выбор определенного типа зависит от требований вашей задачи. """


# Создание массива со всеми цветами шерсти
# wool_colors = [
#     (0, "белый"),
#     (1, "оранжевый"),
#     (2, "пурпурный"),
#     (3, "голубой"),
#     (4, "желтый"),
#     (5, "лайм"),
#     (6, "розовый"),
#     (7, "серый"),
#     (8, "светло-серый"),
#     (9, "голубой"),
#     (10, "фиолетовый"),
#     (11, "синий"),
#     (12, "коричневый"),
#     (13, "зеленый"),
#     (14, "красный"),
#     (15, "черный")
# ]
# for color in wool_colors:
    # print(f"ID: {color[0]}, Цвет: {color[1]}")

# Миссия: Построим столб из блоков внутри массива
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# oneDimensionalRainbowList = [0, 1, 2, 3, 4, 5]
# pos = mc.player.getTilePos()
# x = pos.x
# y = pos.y
# z = pos.z
# for color in oneDimensionalRainbowList:
#     mc.setBlock(x+1, y, z, 35, color)
#     y += 1

# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# twoDimensionalRainbowList = [[0, 0, 0],
#                              [1, 1, 1],
#                              [2, 2, 2],
#                              [3, 3, 3],
#                              [4, 4, 4],
#                              [5, 5, 5]]
# x, y, z = mc.player.getPos()
# startingX = x
# for row in twoDimensionalRainbowList:
#     for color in row:
#         mc.setBlock(x, y, z, 35, color)
#         x += 1
#     y += 1
#     x = startingX

# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# pos = mc.player.getTilePos()
# x, y, z = pos.x, pos.y, pos.z

# blocks = [[35, 35, 22, 22, 22, 22, 35, 35],
#           [35, 22, 35, 35, 35, 35, 22, 35],
#           [22, 35, 22, 35, 35, 22, 35, 22],
#           [22, 35, 35, 35, 35, 35, 35, 22],
#           [22, 35, 22, 35, 35, 22, 35, 22],
#           [22, 35, 35, 22, 22, 35, 35, 22],
#           [35, 22, 35, 35, 35, 35, 22, 35],
#           [35, 35, 22, 22, 22, 22, 35, 35]]

# for row in reversed(blocks):
#     for block in row:
#         mc.setBlock(x, y, z, block)
#         x += 1
#     y += 1
#     x = pos.x