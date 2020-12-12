import math

def getAngle(x,y):
    return math.atan2(y,x) * 180 / math.pi

def getCoordinates(angle, x,y):
    distance = math.sqrt(x**2 + y**2)
    newx = math.cos(angle * math.pi / 180) * distance
    newy = math.sin(angle * math.pi / 180) * distance
    return (newx,newy)

def main():
    instructions = open("input12.txt", "r").read().strip().split("\n") 
    instructions = [[instruction[0], instruction[1:]] for instruction in instructions]
    waypointXpos = 10
    waypointYpos = 1

    boatXpos = 0
    boatYpos = 0

    for instruction in instructions:
        command = instruction[0]
        arg     = int(instruction[1])

        if command == 'N':
            waypointYpos += arg
        elif command == 'S':
            waypointYpos -= arg
        elif command == 'E':
            waypointXpos += arg
        elif command == 'W':
            waypointXpos -= arg
        elif command == 'L':
            oldAngle = getAngle(waypointXpos,waypointYpos)
            newAngle = oldAngle + arg
            waypointXpos, waypointYpos = getCoordinates(newAngle, waypointXpos,waypointYpos)
        elif command == 'R':
            oldAngle = getAngle(waypointXpos,waypointYpos)
            newAngle = oldAngle - arg
            waypointXpos, waypointYpos = getCoordinates(newAngle, waypointXpos,waypointYpos)
        elif command == 'F':
            boatXpos += waypointXpos * arg
            boatYpos += waypointYpos * arg
    print(abs(boatXpos) + abs(boatYpos))

main()