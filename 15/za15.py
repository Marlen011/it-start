# mis1
# def multiply(start, end):
#     result = 1
#     for i in range(start, end + 1):
#         result *= i
#     return result
# result = multiply(4, 6)
# print(result)

# mis2
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# square = 4
# block = 41
# x, y, z = mc.player.getPos()
# mc.setBlocks(x, y, z,
#              x + square, y + square, z + square, block)

# mis3
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# krest_height = 4
# block = 95, 15
# x, y, z = mc.player.getPos()
# mc.setBlocks(x, y, z,
#              x, y + krest_height, z, block)
# mc.setBlocks(x, y + krest_height - 1, z - 1,
#              x, y + krest_height - 1, z + 1, block)

# Рисуем медицинский крест с помощью черепашки
# from mcpi.minecraft import Minecraft
# from minecraftstuff import MinecraftDrawing, MinecraftShape, MinecraftTurtle
# from mcpi import block
# import time

# mc = Minecraft.create()
# pos = mc.player.getTilePos()
# steve = MinecraftTurtle(mc, pos)
# steve.penblock(169)
# for i in range(12):
#     steve.forward(15)
#     if i == 0 or i == 3 or i == 6 or i == 9:
#         steve.left(90)
#     else:
#         steve.right(90)

# mis4
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# import random
# import keyboard

# def randomBlockLocations(blockType, repeats):
#     x, y, z = mc.player.getTilePos()

#     count = 0
#     while count <= repeats:
#         count += 1
#         x += random.randint(-10, 10)
#         z += random.randint(-10, 10)
#         y = mc.getHeight(x, z)
#         mc.setBlock(x, y, z, blockType)

# if __name__ == "__main__":
#     while not keyboard.is_pressed('q'):
#         randomBlockLocations(blockType=47, repeats=50)

# mis6
# from mcpi.minecraft import Minecraft
# import keyboard
# mc = Minecraft.create()

# # создаем функция которая будет генерировать пирамиду
# # передаем аргументами тип блока и высоту пирамиды
# def pyramid(block: int, height: int):
#     x, y, z = mc.player.getTilePos()
#     x, y, z = x + height, y, z
#   # задаем переменную для цвета
#     color = -1
#     # цикл для генерации пирамиды
#     for level in reversed(range(height)):
#       # создаем конструкцию для обновления цвета
#         if color > 15:
#             color = 0
#         color += 1
#         # устанавливаем блоки
#         mc.setBlocks(x - level, y, z - level,
#                      x + level, y, z + level, block, color)
#         # увеличиваем высоту
#         y += 1
# # запускаем бесконечный цикл
# while True:
#   # запускаем функцию при нажатии клавиши q
#     if keyboard.is_pressed("q"):
#         pyramid(block=35, height=5)
#   # останавливаем цикл при нажатии клавиши m
#     elif keyboard.is_pressed("m"):
#         break

# mis7
# from mcpi.minecraft import Minecraft
# import keyboard
# import random
# mc = Minecraft.create()

# def pyramid(height: int):
#     x, y, z = mc.player.getTilePos()
#     x, y, z = x + height, y, z
#     for level in reversed(range(height)):
#         block = random.randint(0, 216)
#         mc.setBlocks(x - level, y, z - level,
#                      x + level, y, z + level, block)
#         y += 1
# while True:
#     if keyboard.is_pressed("q"):
#         pyramid(height=5)
#     elif keyboard.is_pressed("m"):
#         break