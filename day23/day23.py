def main():
    cupsPART1 = [int(num) for num in '469217538'] #Starting order
    cupsPART2 = cupsPART1 + [num for num in range(max(cupsPART1)+1,1000001)]      #Append remaining numbers up to one million
    cupsPART1, cupsPART2 = Cycle(cupsPART1), Cycle(cupsPART2)
   
    cupsPART1.play(100)
    print('Answer Part1:')
    cupsPART1.print()
    cupsPART2.play(10000000) 
    print('Answer Part2: \n', cupsPART2.getAnswePart2())

class Cycle:                    #Uses a array on form arr[cup] = nextCup. 
    def __init__(self, cups):
        self.MAX = len(cups)        
        self.cycle = [0] * (self.MAX + 1)   
        for i in range(len(cups)-1):        #Fill array on form arr[cup] = nextCup
            c = cups[i]
            nextCup = cups[i+1]
            self.cycle[c] = nextCup
        self.cycle[cups[-1]] = cups[0]      #Point last cup at the first one, making a cycle
        self.currentCup = cups[0]           #Set currentCup as the first one in the list

    def play(self, rounds):                     
        for i in range(rounds):             
             #Start by removing three cups following currentCup.
            r1 = self.cycle[self.currentCup]       
            r2 = self.cycle[r1]
            r3 = self.cycle[r2]    
        
            self.cycle[self.currentCup] = self.cycle[r3] # This is done by updating currentCup to the point at the forth cup

            destination = self.currentCup - 1     
            while destination < 1 or destination == r1 or destination == r2 or destination == r3:      #Follows rules to calculate where to insert the three removed cups
                if destination == 0:
                    destination = self.MAX
                else:
                    destination -= 1

            self.cycle[r3] = self.cycle[destination]     #Update the last of the three removed cups to point at the cup destination points at.  the cup that the destination points at.
            self.cycle[destination] = r1                #Update destination to point at the first cup of the three removed. 

            self.currentCup = self.cycle[self.currentCup]  #Update CurrentCup

    def getAnswePart2(self):            #Just a handy method to return the answer for part 2. Gets the number of the two cups following cup 1 and multiplies them. 
        following = self.cycle[1]
        return following * self.cycle[following]

    def print(self):                    #Handy print function. CurrentCup is marked with ()
        s = 'Cups: (' + str(self.currentCup) + ') '
        nextCup = self.cycle[self.currentCup]
        while nextCup != self.currentCup:
            s += str(nextCup) + ' '
            nextCup = self.cycle[nextCup]
        print(s + '\n')
main()
