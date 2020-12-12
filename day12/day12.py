import math

def main():
    instructions = open("input12.txt", "r").read().strip().split("\n") 

    #PART 1
    pos = 0+0j
    direction = 1+0j

    for instruction in instructions:
        command = instruction[0]
        arg     = int(instruction[1:])

        if command == 'N':
            pos += 1j * arg
        elif command == 'S':
            pos -= 1j * arg
        elif command == 'E':
            pos += 1 * arg
        elif command == 'W':
            pos -= 1 * arg
        elif command == 'L':
            steps = int(arg/90)
            for _ in range(steps):
                direction *= 1j 
        elif command == 'R':
            steps = int(arg/90)
            for _ in range(steps):
                direction *= -1j
        elif command == 'F':
            pos += direction * arg

    print("Part1:", abs(pos.real) + abs(pos.imag))

    #PART 2
    currentPos = 0 + 0j
    waypoint = 10 + 1j

    for instruction in instructions:
        command = instruction[0]
        arg     = int(instruction[1:])

        if command == 'N':
            waypoint += 1j * arg
        elif command == 'S':
            waypoint -= 1j * arg
        elif command == 'E':
            waypoint += 1 * arg
        elif command == 'W':
            waypoint -= 1 * arg
        elif command == 'L':
            steps = int(arg/90)
            for _ in range(steps):
                waypoint *= 1j 
        elif command == 'R':
            steps = int(arg/90)
            for _ in range(steps):
                waypoint *= -1j
        elif command == 'F':
            currentPos += waypoint * arg

    print("Part2:", abs(currentPos.real) + abs(currentPos.imag))

main()