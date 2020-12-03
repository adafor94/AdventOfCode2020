import fileinput

def read_input(filename):
    matrix = []

    myFile = open(filename, "r")
    myLine = myFile.readline()
    while myLine:
        matrix.append(myLine.strip())
        myLine = myFile.readline()
    myFile.close()
      
    return matrix     

def main():
    matrix = read_input("input3.txt")
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    TotalCount = 1

    for x in slopes:
        i = 0
        j = 0
        treesThisSlope = 0    
        while(j < len(matrix)):
            treesThisSlope += matrix[j][i] == '#'
            i = (i+x[0])%31
            j += x[1]

        TotalCount *= treesThisSlope
    print(TotalCount)
main()