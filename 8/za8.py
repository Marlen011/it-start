# # mis1
# number1 = int(input())
# number2 = int(input())
# number3 = int(input())

# if number1 > number2 and number1 > number3:
# 	print('num1 biggest')
# elif number2 > number3:
# 	print('num2 biggest')
# else:
# 	print('num3 biggest')
    
# mis2
# print(True and True)
# print(False and False)
# print(True and False)

# mis3
# print(True or False)
# print(False or False)
# print(False or False)

# mis4
# print(not True or True)
# print(not False or False) # error. кажись не продумали тут
# print(not True or False)
# print(not False and True)
# print(not False and not False)
# print(True and False)

# mis6
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()

# x,y,z = mc.player.getPos()
# y-=1
# for i in range(2):
#     block_id = mc.getBlock(x,y,z)
#     if block_id == 80 or block_id == 78:
#         print('player on snow\nblock_id:', block_id)
#         break
#     y+=1
# mc.postToChat(block_id == 80 or block_id == 78)