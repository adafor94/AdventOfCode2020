from collections import deque
import copy

def main():
    directions = open("input24.txt", "r").read().strip().split('\n')
    black = set()       #Set of all black squares

    for d in directions:
        x, y = 0.0, 0.0
        d = deque(d)
        while d: 
            c = d.popleft()
            if c == 'e':
                x += 1
            elif c == 'w':
                x -= 1
            elif c == 's':
                y -= 1
                c = d.popleft()
                if c == 'w':
                    x -= 0.5
                if c == 'e':
                    x += 0.5
            elif c == 'n':
                y += 1
                c = d.popleft()
                if c == 'w':
                    x -= 0.5
                if c == 'e':
                    x += 0.5
            t = tuple((x,y))        #Resulting position

        if t in black:              #If visited before - flip back to white aka remove from black-set
            black.remove(t)
        else: 
            black.add(t)
    print('Answer Part1:', len(black))      #Print amount of black tiles

    DAYS = 100      #PART2                  
    for i in range(1, DAYS+1):
        b = copy.copy(black)                #Make copy of grid
        dictOfWhiteTilesWithBlackAdjacent = {}  #Dict on form whiteTile -> numberOfAdjacentBlackTiles
        for tile in black:
            adja = getAdjacent(tile)        #Get adjacent tiles
            numberOfBlackAdjacent = 0          
            for a in adja:                  #For every adjacent tile
                if a in black:
                    numberOfBlackAdjacent += 1  #If tile is black, increase count
                else:
                    currentCount = dictOfWhiteTilesWithBlackAdjacent.get(a) #If tile is white ...
                    if currentCount == None:                        #If not in dict insert with value 1
                        dictOfWhiteTilesWithBlackAdjacent[a] = 1
                    else:
                        dictOfWhiteTilesWithBlackAdjacent[a] = currentCount + 1 #If alreade in dict, increase count
            if numberOfBlackAdjacent == 0 or numberOfBlackAdjacent > 2:     #If number of adjacent is 0 or more than 2..
                b.remove(tile)                  #Flip from black to white
        for k in dictOfWhiteTilesWithBlackAdjacent.keys():
            if dictOfWhiteTilesWithBlackAdjacent[k] == 2:   #If white tile has two black adjacent, flip from white to black
                b.add(k)
        black = b                                       #Update grid
    print('Answer Part2:', len(black))

def getAdjacent(tile):
    x = tile[0]
    y = tile[1]
    return [tuple((x+dx, y+dy)) for dx,dy in [(1,0), (-1,0), (0.5,-1), (-0.5,-1), (0.5,1), (-0.5,1)]]

main()