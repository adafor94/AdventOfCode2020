import math

def main():
    instructions = [instruction.split(' ') for instruction in open("input14.txt", "r").read().strip().split("\n")]
    mem = {} #Memory [adress,value]
    mask = 0 #Current mask

    #PART 1
    for instruction in instructions:
        if instruction[0] == 'mask': #Update mask
            mask = instruction[2]
        elif instruction[0][0:3] == 'mem': #If memory instruction
            adress = instruction[0][4:-1]   #Get adress
            valueAsBinary = ('0' * len(mask)) + format(int(instruction[2]), 'b') #As binary with buffert of leading zeroes
            result = '' #Result binary number built backwards
            for i in range(1, len(mask) + 1):   #Used to iterate backwards
                if mask[-i] == 'X':             #If 'x' then add bit from valueAsBinary
                    result = valueAsBinary[-i] + result
                else:                           #Else add bit from mask
                    result = mask[-i] + result
            mem[adress] = int(result,2)         #Add result to memory
        else:           #Error check
            print(instruction)

    print("Part1:", sum(mem.values()))          #Print sum of all values hold in memory

    #PART 2
    mem = {} # Empty memory
    for instruction in instructions:
        if instruction[0] == 'mask':            #Update mask
            mask = instruction[2]
        elif instruction[0][0:3] == 'mem':
            adressAsBinary = ('0' * len(mask)) + format(int(instruction[0][4:-1]), 'b') #As binary with buffert of leading zeroes
            value = int(instruction[2])         #Get value
            results = ['']                      #List of adresses
            for i in range(1, len(mask) + 1):
                if mask[-i] == '0':             #If mask == '0' add bit from adress to all adresses in results
                    results = [adressAsBinary[-i] + result for result in results]
                elif mask[-i] == '1':           #If mask == '1' add 1  to al ladresses in results
                    results = ['1' + result for result in results]
                elif mask[-i] == 'X':           #If mask == 'X' add floating bit. -> add '0' to one copy. add '1' to another. Add lists together. 
                    temp1 = ['0' + result for result in results]
                    temp2 = ['1' + result for result in results]
                    results = temp1 + temp2
            for adress in results:      #Add value to each adress
                mem[int(adress,2)] = value
        else:           #Error check
            print(instruction)
    print("Part2:", sum(mem.values()))  #Print sum of all values in memory
main()