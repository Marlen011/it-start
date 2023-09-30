from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
chat_minecraft = None
block_id = mc.getBlock(x,y-1,z)
# Игрок на дереве: True/False
if block_id == 18:
    chat_minecraft = 'Игрок на дереве: True'
    mc.postToChat(chat_minecraft)
else:
    chat_minecraft = 'Игрок на дереве: False'
    mc.postToChat(chat_minecraft)

# Игрок в воде: True/False
if block_id == 8 or block_id == 9:
    chat_minecraft = 'Игрок в воде: True'
    mc.postToChat(chat_minecraft)
else:
    chat_minecraft = 'Игрок в воде: False'
    mc.postToChat(chat_minecraft)

# Игрок в лаве: True/False
if block_id == 10 or block_id == 11:
    chat_minecraft = 'Игрок в лаве: True'
    mc.postToChat(chat_minecraft)
else:
    chat_minecraft = 'Игрок в лаве: False'
    mc.postToChat(chat_minecraft)

# Игрок под землей: True/False
block_id = mc.getBlock(x,y+2,z)
if block_id != 0:
    chat_minecraft = 'Игрок под землей: True'
    mc.postToChat(chat_minecraft)
else:
    chat_minecraft = 'Игрок под землей: False'
    mc.postToChat(chat_minecraft)

# Игрок над землей: True/False
block_id = mc.getBlock(x,y-1,z)
if block_id != 0:
    chat_minecraft = 'Игрок над землей: False'
    mc.postToChat(chat_minecraft)
else:
    chat_minecraft = 'Игрок над землей: True'
    mc.postToChat(chat_minecraft)

# Игрок на снегу: True/False
y-=1
for i in range(2):
    block_id = mc.getBlock(x,y,z)
    if block_id == 80 or block_id == 78:
        chat_minecraft = 'Игрок на снегу: True'
        mc.postToChat(chat_minecraft)
        break
    y+=1
else:
    chat_minecraft = 'Игрок на снегу: False'
    mc.postToChat(chat_minecraft)

# Расстояние до дома: Число блоков
import time
print(x,y,z)
home_x = x
home_y = y
home_z = z
mc.setBlocks(x-1,y-2,z-1,
             x+1,y-2,z+1, 57)
mc.setBlock(x,y-1,z, 138)
for _ in range(3):
    player_x, player_y, player_z = mc.player.getTilePos()
    distance = ((player_x - home_x) ** 2 + (player_y - home_y) ** 2 + (player_z - home_z) ** 2) ** 0.5
    print("Расстояние от дома:", distance)
    time.sleep(5)
print(player_x,player_y,player_z)