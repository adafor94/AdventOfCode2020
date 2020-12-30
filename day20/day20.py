import math
import queue
import copy

def main():
    parsedInput = open("test.txt", "r").read().strip().split('\n\n')
    SIDELENGTH = int(math.sqrt(len(parsedInput)))
    tiles = {}

    for tile in parsedInput:
        tile = tile.split('\n')
        tileID = tile[0].split(' ')[1][0:-1]
        matrix = [row for row in tile[1:]]
        tiles[tileID] = getMutations(matrix)

 #   matches = getAllMatches(tiles)

    result = buildImage(tiles, [], set(), SIDELENGTH)
    print(result)

#def getAllMatches(tiles):


def buildImage(tiles, used, usedKeys, SIDELENGTH):
    if len(used) == len(tiles):
        return (True, '')
    result = ''
    keys = tiles.keys()
    u = copy.copy(used)
    uk = copy.copy(usedKeys)
    for key in keys:
        if key not in usedKeys:
            t = tiles[key]
            i = 0
            while i < len(t):
                if tileIsOk(t[i], u, SIDELENGTH):
                    u.append(t[i])
                    uk.add(key)
                    restOfImage = buildImage(tiles,u, uk, SIDELENGTH)
                    if restOfImage[0]: 
                        return (True, key + ' ' + restOfImage[1])
                    else: 
                        u = u[:-1]
                        uk.remove(key)
                i += 1
    return (False, 'FAIL')

def tileIsOk(tile, used, SIDELENGTH):
    top = getTopSide(tile)
    left = getLeftSide(tile)
    pos = len(used)
    if pos == 0:
        return True
    elif pos in range(1, SIDELENGTH):
        #Check left
        return left == getRightSide(used[-1])
    elif pos % SIDELENGTH == 0:
        #Check top
        above = pos - SIDELENGTH
        return top == getDownSide(used[above])
    else: 
        #Check top and left
        above = pos - SIDELENGTH
        return (top == getDownSide(used[above]) and (left == getRightSide(used[-1])))

def getMutations(m):
    mutations = [m]
    mutations.append(flipMatrixY(m))
    temp = m
    for i in range(3):      #Add rotated and flipped
        rotated = rotateMatrixClockWise(temp)
        mutations.append(temp)
        mutations.append(flipMatrixY(rotated))
        temp = rotated
    return mutations

def flipMatrixX(m):
    newM = []
    for j in range(len(m)):
        temp = ''
        for i in range(len(m[0])-1,-1,-1):
            temp += m[j][i]
        newM.append(temp)
    return newM

def rotateMatrixClockWise(m):
    newM = []
    for j in range(len(m)):
        temp = ''
        for i in range(len(m[0])-1,-1,-1):
            temp += m[i][j]
        newM.append(temp)
    return newM

def flipMatrixY(m):
    newM = []
    for i in range(len(m[0])-1,-1,-1):
        temp = ''
        for j in range(len(m)):
            temp += m[i][j]
        newM.append(temp)
    return newM

def getTopSide(m):
    return m[0] 

def getRightSide(m):
    temp = ''
    for i in range(len(m)):
        temp += m[i][-1]
    return temp

def getDownSide(m):
    return m[-1]

def getLeftSide(m):
    temp = ''
    for i in range(len(m)):
        temp += m[i][0]
    return temp

def printMatrix(m):
    for row in m:
        print(row)

def printAllMutations(ms):
    for m in ms:
        printMatrix(m)
        print()

main()