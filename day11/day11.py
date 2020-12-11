import fileinput

def main():
    seats = open("input11.txt", "r").read().strip().split("\n") #Make a list of the seats for each row
    hasChanged = True
    rows = len(seats)
    cols = len(seats[0])
    while hasChanged:
        seatsOfNextGeneration = [''] * rows
        hasChanged = False
        for i in range(0,rows):
            for j in range(0, cols):
                oldSeat = seats[i][j]
                newSeat = checkSeat(seats,i,j,1)
                if newSeat != oldSeat:
                    hasChanged = True
                seatsOfNextGeneration[i] += newSeat
        seats = seatsOfNextGeneration

    ans = 0
    for row in seats:
        for i in range(0, cols): 
            if row[i] == '#':
                ans += 1
    print(ans)

def checkSeat(seats, i,j, part):
    seat = seats[i][j]
    if seat == '.':
        return '.'

    count = 0
    limit = 0
    affectedSeats = []
    if part == 1:
        affectedSeats = getAffectedSeats(seats,i,j)
        limit = 4
    else:
        affectedSeats = getAffectedSeats2(seats,i,j)
        limit = 5
    if i == 0 and j == 6:
        print(affectedSeats)
    for r,c in affectedSeats:
        if seats[r][c] == '#':
            if seat == 'L':
                return 'L'
            elif seat == '#':
                count += 1
    if count >= limit:
        return 'L'

    return '#'

def getAffectedSeats(seats,i,j):
    neighbours = []
    for a in range(-1,2):
        for b in range(-1,2):
            r = i+a
            c = j+b 
            if 0 <= r < len(seats) and 0 <= c < len(seats[0]) and not (a==0 and b==0):
                neighbours.append([r,c])
    return neighbours

def getAffectedSeats2(seats, i,j):
    temp = 0
    neighbours = getAffectedSeats(seats,i,j)
    for r,c in neighbours:
        if seats[r][c] == '.':
            di = r - i
            dj = c - j
            if di > 1: 
                di = 1
            elif di < -1:
                di = -1
            if dj > 1:
                dj = 1
            elif dj < -1:
                dj=-1

            a = r + di
            b = c + dj
            if 0 <= a < len(seats) and 0 <= b < len(seats[0]) and not (i==r and j==c):
                neighbours.append([a, b])
    return neighbours

main()
