import os
import random
import time

""" These variables will be used for generating the digital rain,
 They are taken from the terminal size. """

WIDTH, HEIGHT = os.get_terminal_size() 
DROPHEIGHT = HEIGHT*2

# These chars will be randomly chosen to generate the rain
# They can be replaced by any other string, such as "01"
SEEDSTR = "abcdefghijklmnopqrstuvwxyz"

# Gets a random letter from the seed
def random_letter(seed):
    return random.choice(seed)

# Fills the list with "raindrops" to be used
raindrops = []
x = 0
while x < WIDTH:
    # Randomly generates the height of the single drop
    maxdrop = random.randrange(HEIGHT, DROPHEIGHT)
    drop = ""
    for i in range(maxdrop):
        drop += random_letter(SEEDSTR)
    for i in range(DROPHEIGHT-maxdrop):
        drop += " "
    raindrops.append(drop)
    x += 1

# To explain the code above, the reason I'm using DROPHEIGHT
# as twice the length of HEIGHT is so that once printed
# the entire height of the terminal can be filled with characters
# instead of the printscreen looking like a "spill"

# Combines the "drops" into printable rows
rows = []
x = 0
while x < DROPHEIGHT:
    row = ""
    for drop in raindrops:
        row += drop[DROPHEIGHT-x-1]
    rows.append(row)
    x += 1

# Prints the rain
curtain = []
for row in rows:
    curtain.insert(0, row)
    time.sleep(0.1)
    os.system("clear")
    for elem in curtain:
        print(elem)

    # Removes the rows at the bottom so the entire screen can be filled
    if len(curtain) > HEIGHT:
        curtain.pop(-1)