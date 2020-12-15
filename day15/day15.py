def main():
    startingNumbers = [int(n) for n in open("input15.txt", "r").read().strip().split(',')]

    ans1 = playGame(startingNumbers, 2020) #PART1
    ans2 = playGame(startingNumbers, 30000000) #PART2
    print(ans1, ans2)

def playGame(startingNumbers, rounds):
    mem = {}    #Key =  number, Value = last round it where spoken

    for i in range(len(startingNumbers)-1):     #Load mem with startingNumbers
        mem[startingNumbers[i]] = i+1

    last = startingNumbers[-1]                  #last = last startingNumber

    for i in range(len(startingNumbers),rounds):
        if last not in mem.keys():              #If the last number had not been spoken before (= not in mem), add it to mem and update last = 0
            mem[last] = i 
            last = 0
        else:                                   #If the last number had been spoken before, take difference between round and last time it where spoken. Update mem and last
            diff = i - mem[last]
            mem[last] = i
            last = diff
    return last #Return last number spoken after x rounds

main()