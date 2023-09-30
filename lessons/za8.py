# mis2
# true and ? = true
# flase and ? = False
# ? and ? = false
# mis3
# ture or ? = true
# false or ? = false
# ? or ? = False
# mis4
# not true or ? = true
# not ? or false = false
# not ? and true = True
# not ? and not ? = True
# ? and ? = false


# mis1
number1 = int(input('num1: '))
number2 = int(input('num2: '))
number3 = int(input('num3: '))

if number1 > number2 and number1 > number3:
	print('num1 biggest')
elif number2 > number3:
	print('num2 biggest')
elif number1 == number2 or number2 == number3 or number3 == number1:
	print('equal')
else:
	print('num3 biggest')
    
# mis2
# print(True and True)
# print(False and False)
# print(True and False)

# # mis3
# print(True or False)
# print(False or False)
# print(False or False)

# mis4
# print("1", not True or True)
# # print(not False or False) # error. кажись не продумали тут
# print("2", not True or False)
# print("3", not False and True)
# print("4", not False and not False)
# print("5", True and False)

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