import math
import queue
import copy

def main():
    originalTiles = open("input20.txt", "r").read().strip().split('\n\n')
    
    originalTiles = [tile.split('\n') for tile in originalTiles]
    originalTiles = [(tile[0].split(' ')[1][0:-1], tile[1:]) for tile in originalTiles] #List on type [(ID, PATTERN)]

    SIDELENGTH = int(math.sqrt(len(originalTiles)))
    SEAMNOSTERPATTERN = [(0,0), (1,-18),(1,-13),(1,-12), (1,-7), (1,-6), (1,-1), (1,0), (1,1), (2,-17),(2,-14),(2,-11), (2,-8), (2,-5), (2,-2)] #Coordinates of seamonster relative to first coordinate
    COLSINTILE = len(originalTiles[0][1][1])
    ROWSINTILE = len(originalTiles[0][1])
    NUMBEROFTILES = len(originalTiles)

    emptyTile = ['-' * COLSINTILE] * ROWSINTILE                     #Empty tile
    imageTiles = [emptyTile] * NUMBEROFTILES                    #Fill imageTiles with emptyTiles to start with
    imageIDs = ['0'] * NUMBEROFTILES                            #Fill imageID with Zeroes to start with


    tiles = {}  # ID -> TILE
    possibleMatches = {} # ID -> MATCHES
    ans1 = 1            #Product of IDs of tiles with 2 matches aka corner-tiles
    corners = []

    for tile in originalTiles:
        tiles[tile[0]] = tile[1]                             
        matches = findNeighbours(tile, originalTiles)
        possibleMatches[tile[0]] = matches
        if len(matches) == 2:
            ans1 *= int(tile[0])
            corners.append(tile[0])

    #PART2
    topLeftCorner = ''          #Find top left corner to start with
    for c in corners:
        sides = findSidesThatHasMatches(c, tiles, possibleMatches)
        if sides == '0110':
            topLeftCorner = c
            break
    
    usedIDs = set()                 #A set of used IDs
    usedIDs.add(topLeftCorner)
    imageTiles[0] = tiles[topLeftCorner]    #Start filling imageTile
    imageIDs[0]   = topLeftCorner           #Start filling imageIDs
    pos = 1
    while pos < NUMBEROFTILES:
        if pos % SIDELENGTH == 0:   #IF at the end of row, get matches from tile above ELSE from tile to the left
            matchingTileIDs = possibleMatches[imageIDs[pos-SIDELENGTH]]
        else:
            matchingTileIDs = possibleMatches[imageIDs[pos-1]]
       
        for tileID in matchingTileIDs:        #Loop through possible
            if tileID not in usedIDs:           #Check if ID is used
                tile = tiles[tileID]            
                version = findVersion(tile, imageTiles, pos, SIDELENGTH)        #Return correct version of tile if one exists, else return False
                if version != False:                    #If a correct version is found update imageTiles, imageIDs and usedIDs
                    imageTiles[pos] = version
                    imageIDs[pos] = tileID
                    usedIDs.add(tileID)
                    break
        pos += 1    #Update pos to find next tile

    tilesWithoutBorders = removeBorders(imageTiles, SIDELENGTH)              #Remove border
    assembled = assembleImage(tilesWithoutBorders, SIDELENGTH)               #Assemble image
  
    # FIND SEAMONSTERS!
    allFinalImages = getMutations(assembled)            #Variations of image
    countHashtags = countSeamonsters = 0
    for image in allFinalImages:                    #Try each variation until seamonsters are found
        countHashtags = 0
        copyImage = copy.copy(image)                #Copy to mark seamonsters for fun
        for i in range(len(image)):                 #Check every index of the picture
            for j in range(len(image[0])):
                if image[i][j] == '#':              #Count number of hashtags for answer for part2
                    countHashtags += 1
                indexes = []                        #Save indexes to mark seamonsters
                for pos in SEAMNOSTERPATTERN:       #For every index of SEAMONSTERPATTERN, calculate coordinates.
                    row, col = i + pos[0], j + pos[1]
                    indexes.append((row,col))
                    if not (0 < row < len(image)) or not (0 < col < len(image[0])-1) or image[row][col] != '#': #If coordinates are out of bounds or the char is not '#' -> break
                        break
                else:   
                    countSeamonsters += 1
                    for index in indexes:
                        copyImage[index[0]] = copyImage[index[0]][0:index[1]] + '0' + copyImage[index[0]][index[1]+1:]
               
        if countSeamonsters != 0:   #If count is 0 try next version of the image, else print image with marked seamonsters and break.
            printMatrix(copyImage) #Print image with seamonsters marked with zeroes. 
            break

    print('Answer Part 1:', ans1)
    print('Answer Part 2:', countHashtags - countSeamonsters * 15)

def assembleImage(imageTiles, SIDELENGTH):
    assembledImage = []
    tileLength = len(imageTiles[0])
    start = 0
    end = SIDELENGTH
    i = 0
    while start < len(imageTiles):
        for i in range(tileLength):
            rows = [tile[i] for tile in imageTiles[start:end]]
            temp = ''
            for r in rows:
                temp += r
            assembledImage.append(temp)
        start = end
        end += SIDELENGTH
    return assembledImage

def removeBorders(imageTiles, SIDELENGTH):
    imageWithoutBorders = copy.copy(imageTiles)
    for i in range(len(imageTiles)):
        tile = imageTiles[i]
        tile = tile[1:-1]
        tile = [row[1:-1] for row in tile]
        imageWithoutBorders[i] = tile
    return imageWithoutBorders

def findSidesThatHasMatches(tileID, tiles, possibleMatches):
    tile = tiles[tileID]
    result = ''
    sides = getTopSide(tile), getRightSide(tile), getDownSide(tile), getLeftSide(tile)
    matches = possibleMatches[tileID]
    allSides = [] 
    for m in matches:
        t = tiles[m]
        allSides += getSides(t)
    for side in sides:
        if side in allSides:
            result += '1'
        else: 
            result += '0'
    return result

def findNeighbours(tile, originalTiles):
    neighbours = []
    tileID, t = tile[0], tile[1]
    sides = [getTopSide(t), getRightSide(t), getLeftSide(t), getDownSide(t)]

    for possibleNeighbour in originalTiles:
        if possibleNeighbour[0] != tileID:
            neighbourSides = getSides(possibleNeighbour[1])
            for side in sides:
                if side in neighbourSides:
                    neighbours.append(possibleNeighbour[0])
                    break
    return neighbours

def findVersion(tile, imageTiles, pos, SIDELENGTH):
    allVersions = getMutations(tile)
    if pos == 0:
        print('STRANGE')
    elif pos in range(1, SIDELENGTH): #Check left
        relevantSide = getRightSide(imageTiles[pos-1])
        for version in allVersions:
            if relevantSide == getLeftSide(version):
                return version
    elif pos % SIDELENGTH == 0:     #Check top
        relevantSide = getDownSide(imageTiles[pos-SIDELENGTH])
        for version in allVersions:
            if relevantSide == getTopSide(version):
                return version
    else: #Check top and left
        above = pos - SIDELENGTH
        relevantSides = [getRightSide(imageTiles[pos-1]), getDownSide(imageTiles[above])]
        for version in allVersions:
            if relevantSides[0] == getLeftSide(version) and relevantSides[1] == getTopSide(version):
                return version
    return False

def getMutations(tile):
    mutations = [tile]
    mutations.append(flipMatrixY(tile))
    temp = tile
    for i in range(3):      #Add rotated and flipped
        rotated = rotateMatrix(temp)
        mutations.append(rotated)
        mutations.append(flipMatrixY(rotated))
        temp = rotated
    return mutations

def rotateMatrix(tile):
    newM = []
    for j in range(len(tile)):
        temp = ''
        for i in range(len(tile[0])-1,-1,-1):
            temp += tile[i][j]
        newM.append(temp)
    return newM

def flipMatrixY(tile):
    newM = []
    for i in range(len(tile[0])-1,-1,-1):
        temp = ''
        for j in range(len(tile)):
            temp += tile[i][j]
        newM.append(temp)
    return newM

def getSides(tile):
    return [getTopSide(tile), getRightSide(tile), getLeftSide(tile), getDownSide(tile), getTopSide(tile)[::-1], getRightSide(tile)[::-1], getLeftSide(tile)[::-1], getDownSide(tile)[::-1]]

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

main()