def main():
    cupsPART1 = [int(num) for num in '469217538'] #Starting order
    cupsPART2 = cupsPART1 + [num for num in range(max(cupsPART1)+1,1000001)]      #Append remaining numbers up to one million
    cupsPART1 = Cycle(cupsPART1)
    cupsPART2 = Cycle(cupsPART2)
   
    cupsPART1.play(100)
    print('Answer Part1:')
    cupsPART1.print()
    print()
    cupsPART2.play(10000000) 
    print('Answer Part2:', cupsPART2.getAnswePart2())

class Cycle:                    #Uses a dictionary to make a linked-list like data structure with quick access. 
    def __init__(self, cups):
        self.MAX = len(cups)        
        self.cycle = {} 
        for i in range(len(cups)-1):        #Map each cup to the next one in the list
            c = cups[i]
            nextCup = cups[i+1]
            self.cycle[c] = nextCup
        
        self.cycle[cups[-1]] = cups[0]      #Map last cup to the first to make a cycle
        self.currentCup = cups[0]           #Set currentCup as the first one in the list
        
    def play(self, rounds):                     #Uncomment for debugging
        for i in range(rounds):
            # print('ROUND:', i+1)
            # self.print()
            removed = self.removeThreeCups()
            # print('Pick up:', removed)
            self.insert(removed)
            self.updateCurrent()
        #     print()
        # print('FINAL')
        # self.print()

    def getAnswePart2(self):            #Just a handy method to return the answer for part 2. Gets the number of the two cups following cup 1 and multiplies them. 
        following = self.cycle[1]
        return following * self.cycle[following]

    def removeThreeCups(self):          #Removing three cups is the same as moving the pointer three steps. Returns a list of the removed cups
        removed = []
        temp = self.currentCup          #Set temp as current cup
        for i in range(3):              #Do three times
            cup = self.cycle[temp]      #Set temp as nextCup
            removed.append(cup)         #Add to list of removed cups
            temp = cup
        self.cycle[self.currentCup] = self.cycle[temp] #Set currentCup to point at nextCup
        return removed                  

    def insert(self, cups):             
        destination = self.currentCup - 1       
        while destination < 1 or destination in cups:          #If destination not in the dictionary = is in cups, decrease by one and try again
            if destination == 0:
                destination = self.MAX
            else:
                destination -= 1
        
     #   print('Destination: ', destination)
        temp = self.cycle[destination]     #Save the cup that destination points at.
        self.cycle[destination] = cups[0] 
        self.cycle[cups[-1]] = temp 

    def updateCurrent(self):                #Simply updating to next cup in the cycle
        self.currentCup = self.cycle[self.currentCup]  

    def print(self):                    #Handy print function. CurrentCup is marked with ()
        s = 'Cups: (' + str(self.currentCup) + ') '
        nextCup = self.cycle[self.currentCup]
        while nextCup != self.currentCup:
            s += str(nextCup) + ' '
            nextCup = self.cycle[nextCup]
        print(s)
main()
