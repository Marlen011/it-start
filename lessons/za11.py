# mis1
# number = 1
# while number < 11:
#     print(number)
#     number+=1

# mis2
# import time
# import random
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# count = 0
# while count < 5:
#     x = random.randint(1500, 1520)
#     y = random.randint(100)
#     z = random.randint(1500, 1520)
#     mc.player.setPos(x,y,z)
#     time.sleep(2)
#     count+=1
#     print(x,z)

# mis3
# import time
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# count = 0
# # water = 9
# lava = 11
# while count < 5:
#     x,y,z=mc.player.getPos()
#     mc.setBlock(x,y,z,lava)
#     count+=1
#     time.sleep(1)

# mis5
# import time
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# flower = 38, 6
# while True:
#     x,y,z=mc.player.getPos()
#     stop_block = mc.getBlock(x,y-1,z)
#     if stop_block == 57:
#         break
#     elif stop_block == 58:
#         time.sleep(10)
#     mc.setBlock(x,y,z,flower)
#     mc.setBlock(x+1,y,z+1,flower)
#     mc.setBlock(x-1,y,z-1,flower)
#     time.sleep(0.3)

# mis6
# import time
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# gold=41
# dimond=57
# while True:
#     x,y,z=mc.player.getTilePos()
#     if mc.getBlock(x+1,y,z) == gold:
#         print('GOLD')
#         break
#     else:
#         mc.setBlock(x,y-1,z,dimond)
#         mc.setBlock(x,y+2,z,dimond)
#         mc.setBlock(x,y,z+1,dimond)
#         mc.setBlock(x,y,z-1,dimond)
#         mc.setBlock(x,y+1,z+1,dimond)
#         mc.setBlock(x,y+1,z-1,dimond)
#         print('uwu')
#         time.sleep(2)