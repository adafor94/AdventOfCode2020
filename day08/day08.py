import fileinput

def main():
    listOfInstructions = [instruction.split(' ') for instruction in open("input8.txt", "r").read().strip().split("\n")]
    ans1 = 0
    pointer = 0
    setOfFlippedInstructions = set()
    flipInstruction = False # Starts as False to get answer for part 1 in first loop. 

    while pointer < len(listOfInstructions):
        pointer = 0
        setOfExecutedInstructions = set()
        accumulator = 0

        while pointer not in setOfExecutedInstructions and pointer < len(listOfInstructions):
            setOfExecutedInstructions.add(pointer)
            inst, arg = listOfInstructions[pointer]
            if inst == 'nop':
                if flipInstruction and pointer not in setOfFlippedInstructions:
                    setOfFlippedInstructions.add(pointer)
                    flipInstruction = False
                    pointer += int(arg)
                else:
                    pointer += 1
            elif inst == 'jmp':
                if flipInstruction and pointer not in setOfFlippedInstructions:
                    setOfFlippedInstructions.add(pointer)
                    flipInstruction = False
                    pointer += 1
                else:
                    pointer += int(arg)
            elif inst == 'acc':
                accumulator += int(arg)
                pointer += 1
        flipInstruction = True
        if ans1 == 0: 
            ans1 = accumulator
    print(ans1, accumulator)

main()