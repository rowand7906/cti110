#Random Number File Writer
#July 5th 2017
#CTI-110 M6HW1
#Dante' Rowan

import random

randfile = open("Randomnm.txt", "w" )

for i in range(int(input('How many to generate?: '))):
    line = str(random.randint(1, 500))
    randfile.write(line)
    print(line)

randfile.close()
