# # mis2
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# x, y, z = mc.player.getTilePos()
# x += 10
# y += 10
# z += 10
# mc.player.setTilePos(x, y, z)

# mis3
# x, y, z = mc.player.getTilePos()
# mc.setBlock(x, y-1, z, 169)

# mis4
# x, y, z = mc.player.getTilePos()
# mc.setBlocks(x-1, y, z-1,
#              x+1, y+3, z+1, 101)
# mc.setBlocks(x, y, z, 	x, y+2, z, 0)

# mis6
# x, y, z = mc.player.getTilePos()
# mc.setBlocks(x+2, y, z-3,		x+8, y+6, z+3, 42) ##mis6
# mc.setBlocks(x+3, y+7, z-2,		x+7, y+11, z+2, 41)
# mc.setBlocks(x+4, y+12, z-1,		x+6, y+14, z+1, 57)
# mc.setBlocks(x+5, y+15, z,		x+5, y+19, z, 169)

# mis7
x, y, z = mc.player.getTilePos()
mc.setBlocks(x+1, y, z,		x+7, y+6, z+6, 42)
mc.setBlocks(x+3, y+7, z+2,		x+5, y+9, z+4, 41)

# mis8
# x, y, z = mc.player.getTilePos()
# mc.setBlocks(x+1, y, z,		x+5, y+6, z+8, 3)
