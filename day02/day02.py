import fileinput

def read_integers(filename):
    myList = []
    myFile = open(filename, "r")
    myLine = myFile.readline()
    while myLine:
        myLine = myLine.split(' ')
        low = myLine[0].split('-')[0]
        high = myLine[0].split('-')[1]
        character = myLine[1][0]
        password = myLine[2]
        myList.append([low,high,character,password])

        myLine = myFile.readline()

    myFile.close()
      
    return myList     

def main():
    myList = read_integers("input2.txt")
    i = 0
    for x in myList:
      #  amount = 0
        low = int(x[0])
        high = int(x[1])
        character = x[2]
        password = x[3]
        if((password[low-1] == character and password[high-1] != character) or (password[low-1] != character and password[high-1] == character)):
            i += 1

    """     for c in password:
            if c == character:
                amount += 1
        if (amount >= low):
            if (amount <= high):
                  i += 1
    """
        
    print(i)
main()