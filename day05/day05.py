import fileinput

def translateToDecimal(s):
    row = s[:-3].replace('F','0').replace('B','1')
    col = s[-3:].replace('L','0').replace('R','1')
    return [int(row,2), int(col,2)]

def read_input(filename):
    boardingpasses = open(filename, "r").read().strip().split("\n")
    temp = [translateToDecimal(x) for x in boardingpasses]
    return temp

def main():
    boardingpasses = read_input("input5.txt")
    listOfIDs = [x[0] * 8 + x[1] for x in boardingpasses]
    listOfIDs.sort()

    index = 0
    while listOfIDs[index+1] == listOfIDs[index] + 1:
        index += 1

    print(listOfIDs[-1], listOfIDs[index]+1)

main()