# Build Basic House uses Minecraft Pi Edition and builds a house based on how many
# blocks tall you want it to be

# Libraries we need
from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()

# Get player's initial position
x, y, z = mc.player.getPos()

# Set the block we want it to be made out of
brick = 43;

# Get info from user
mc.postToChat("Look at the terminal.")
n =0
height =  input("How many blocks tall? #")

# We want the player, who is 2 blocks tall, to fit with no problem
height = int(height) +  2
mc.postToChat("Building basic house...")

# Have the house be 5 blocks in front of them
x = x + 6

# Set the origonal x position so that we don't lose it
orgx = x

# Wait a bit for the user to see the action happen
sleep(2)
n = 0

# Use a loop to make the code look clean
for n in range(1, height):
    m = 0
    
    # Start setting blocks, 20 blocks on each side
    for m in range(1, 21):
        mc.setBlock(x, y, z, brick)
        x += 1
        
        # wait so that the user can watch in awe as their house is literally
        # drawn out in front of them
        sleep(0.1)
    # Reset the counter
    m = 0
    
    # One more block, turn 90 degrees, then do it again
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
    
    # Move one block up, reset x, then do it again
    y += 1
    x = orgx

# Now it is time to make the roof. Put the variables so we start again in the right place, then do it again
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
# Afterwards there is one hole in their roof. Make sure the user fills it in.
