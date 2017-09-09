import numpy as np

path = "input.txt"

leftTurnCount = 0
penaltySize = 0

with open(path) as file:
    line = file.readline().split(sep='=')
    if line[0] != "penalty":
        print("Couldn't find penalty size.")
        exit(-1)

    penaltySize = float(line[1])
    beforeTurnCoord = np.fromstring(file.readline(), sep=' ')
    movementVector = np.array([0.0, 0.0])

    for line in file:
        afterTurnCoord = np.fromstring(line, sep=' ')
        turnVector = afterTurnCoord - beforeTurnCoord

        cross = np.cross(movementVector, turnVector)
        if cross > 0:
            leftTurnCount += 1

        movementVector = turnVector
        beforeTurnCoord = afterTurnCoord

print("Total penalty: {}".format(penaltySize * leftTurnCount))