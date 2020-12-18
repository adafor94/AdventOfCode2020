import copy

def main():
    parsedInput = open("input17.txt", "r").read().strip().split('\n')
    activityMatrix = {}
    #Keep track of borders of the matrix
    xMin = 0
    xMax = len(parsedInput[0]) -1
    yMin = 0
    yMax = len(parsedInput) -1
    zMin = 0
    zMax = 0
    wMin = 0
    wMax = 0

    ROUNDS = 6 #Number of rounds

    #Fill matrix with starting values
    for row in range(yMax + 1):
        for col in range(xMax + 1):
            activityMatrix[row,col,0,0] = parsedInput[row][col]

    #Simulate
    for _ in range(ROUNDS):
        newMatrix = copy.deepcopy(activityMatrix) #Make copy
        
        for x in range(xMin-1, xMax + 2):
            for y in range(yMin-1, yMax + 2):
                for z in range(zMin-1, zMax + 2):
                    for w in range(wMin-1, wMax + 2): #loop through all indexes
                        activeNeighbours = 0

                        for xDelta in [-1,0,1]:
                            for yDelta in [-1,0,1]:
                                for zDelta in [-1,0,1]:
                                    for wDelta in [-1,0,1]: #For all neighbours ... check if active 
                                        if not (xDelta == 0 and yDelta == 0 and zDelta == 0 and wDelta == 0):
                                            if (x+xDelta, y+yDelta, z+zDelta, w+wDelta) in activityMatrix.keys():
                                                if activityMatrix[x+xDelta, y+yDelta, z+zDelta, w+wDelta] == '#':
                                                    activeNeighbours += 1
                        #RULES
                        if (x,y,z,w) in activityMatrix.keys() and activityMatrix[x,y,z,w] == '#': #If active and not 2 or 3 neighbours are active it becomes inactive
                            if not (activeNeighbours == 2 or activeNeighbours == 3):
                                newMatrix[x,y,z,w] = '.'
                        elif activeNeighbours == 3:                     #If inactive and 3 active neighbours it becomes active
                                newMatrix[x,y,z,w] = '#'   
    

        #UPDATE BOARDER OF MATRIX
        xMin -= 1
        xMax += 1
        yMin -= 1
        yMax += 1
        zMin -= 1
        zMax += 1
        wMin -= 1
        wMax += 1

        activityMatrix = newMatrix   
        
    ans = 0
    for v in activityMatrix.values():
        if v == '#':
            ans += 1
    
    #FOR PART 1 answer simply remove anything that has to do with w (4th dimension)

    print(ans)
main()

  