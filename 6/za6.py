# # mis1
# number = int(input())
# number2 = int(input())
# if number > number2:
#     print('число 1 больше числа 2')
# if number > number2*2:
#     print('число 1 в 2 раза больше числа 2')

# mis2
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()

# x, y, z = mc.player.getTilePos()
# position = x, y+2, z
# block_id = mc.getBlock(*position) #В данном коде знак * перед переменной position выполняет распаковку (unpacking) списка координат, передавая их в качестве отдельных аргументов функции getBlock().
# print(block_id)

# mis3
# print(500==500)
# print(500!=500)
# print(900==500)
# print(1000<2000)
# print(0<-100)
# print(-100==-200)
# print(-200==-200)

# # mis4
# x, y, z = mc.player.getPos()
# block_id = mc.getBlock(x, y, z)
# print(block_id)
# if block_id == 10 or block_id == 11:
#     print("Игрок находится в лаве.")
# else:
#     print("Игрок не находится в лаве.")

# mis5
# x,y,z = mc.player.getPos()
# if y < 60:
#     print('player under world')
# else:
#     print('player above world')

# x,y,z = mc.player.getPos()
# block_id = mc.getBlock(x,y+2,z)
# if block_id != 0:
#     print('игрок под землей')
# else:
#     print('игрок на земле')

# mis7
# from mcpi.minecraft import Minecraft
# import time
# mc = Minecraft.create()
# x,y,z = mc.player.getTilePos()
# print(x,y,z)
# home_x = x
# home_y = y
# home_z = z
# for _ in range(3):
#     player_x, player_y, player_z = mc.player.getTilePos()
#     distance = ((player_x - home_x) ** 2 + (player_y - home_y) ** 2 + (player_z - home_z) ** 2) ** 0.5
#     print("Расстояние от дома:", distance)
#     time.sleep(10)
# print(player_x,player_y,player_z)
