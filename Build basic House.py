from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
x, y, z = mc.player.getPos()
brick = 43;
mc.postToChat("Look at the terminal.")
n =0
height =  input("How many blocks tall? #")
height = int(height) +  2
mc.postToChat("Building basic house...")
x = x + 6
orgx = x
sleep(2)
n = 0
for n in range(1, height):
    m = 0
    for m in range(1, 21):
        mc.setBlock(x, y, z, brick)
        x += 1
        sleep(0.1)
    m = 0
    mc.setBlock(x, y, z, brick)
    z += 1
    for m in range(1, 21):
        mc.setBlock(x, y, z, brick)
        z += 1
        sleep(0.1)
    m = 0
    mc.setBlock(x, y, z, brick)
    x -= 1
    for m in range(1, 21):
        mc.setBlock(x, y, z, brick)
        x -= 1
        sleep(0.1)
    mc.setBlock(x, y, z, brick)
    m = 0
    z -= 1
    for n in range(1, 21):
        mc.setBlock(x, y, z, brick)
        z -= 1
        sleep(0.1)
    mc.setBlock(x, y, z, brick)
    y += 1
    x = orgx
m = 0
x += 1
z -= 1
y -= 1
for m in range(1, 21):
    n = 0
    z += 2
    x = orgx + 1
    for n in range(1, 19):
        mc.setBlock(x, y, z, brick)
        x += 1
        n += 1
    n = 0
    mc.setBlock(x, y, z, brick)
    z -= 1
    x -= 1
    for n in range(1, 19):
        mc.setBlock(x, y, z, brick)
        x -= 1
        n += 1
    n = 0
    mc.setBlock(x, y, z, brick)
x -= 1
mc.setBlock(x, y, z, brick)
