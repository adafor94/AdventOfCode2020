import fileinput

d = {} # empty dict for memoization

def main():
    listOfNumbers = [int(n) for n in open("input10.txt", "r").read().strip().split("\n")] #Make a list of the numbers
    listOfNumbers.sort()

    last = ones = threes = 0
    for n in listOfNumbers: #Check the difference between n and last 
        d = n - last
        if d == 1:
            ones += 1
        elif d == 3:
            threes += 1
        last = n
    
    print(ones * (threes + 1))
    print(ways(listOfNumbers,listOfNumbers[-1]))
        
def ways(listOfNumbers, n):     # For any n, the number of ways to go through the graph from n to zero is equal to the sum of number of ways from the children of n to zero. 
    if n in d:                  # Checks if ways(n) has been calculated before. Memoization
        return d[n]

    count = 0
    for i in range(1,4):
        if n-i == 0:
            count += 1
        elif n-i in listOfNumbers:
            count += ways(listOfNumbers, n-i)
    d[n] = count
    return(count)

main()