import fileinput

def main():
    listOfNumbers = [int(n) for n in open("input9.txt", "r").read().strip().split("\n")] #Make a list of the numbers

    preample = listOfNumbers[0:25]              
    decryptedNumbers = listOfNumbers[25:]

    n = decryptedNumbers.pop(0)
    while approved(n, preample): #check each number until we find a illegal one
        preample.pop(0)
        preample.append(n)
        n = decryptedNumbers.pop(0)
    ans1 = n

    #Part2
    lowIndex = highIndex = 0
    tot = int(listOfNumbers[0])

    #lowIndex and highIndex describe the boarders of the set. 
    # If tot is too small, highIndex is increased. If tot is too big, lowIndex is increased.
    while tot != ans1:
        if tot < ans1:
            highIndex += 1
            tot += int(listOfNumbers[highIndex])
        else:
            tot -= int(listOfNumbers[lowIndex])
            lowIndex += 1

    ans2 = min(listOfNumbers[lowIndex:highIndex+1]) + max(listOfNumbers[lowIndex:highIndex]))  #Add min and max of found set together to produce ans2
    print(ans1,ans2)      

def approved(n, preample):  #Check if two numbers in the list equals n. Could sort preample and do it in O(n) but since it's just 25 numbers i don't bother atm. 
    for i in range(25):
        for j in range(i+1,25):
            if preample[i] + preample[j] == n:
                return True
    return False

main()