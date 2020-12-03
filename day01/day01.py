import fileinput

def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]        

def main():
    myList = read_integers("input1.txt")

    for x in range(len(myList)):
        for y in range(x, len(myList)):
            for z in range(y, len(myList)):
                if (myList[x] + myList[y] + myList[z]== 2020):
                    print(myList[x] * myList[y] * myList[z])

main()