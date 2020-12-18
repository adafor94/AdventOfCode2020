def main():
    parsedInput = open("input16.txt", "r").read().strip().split('\n\n')
    fields = parsedInput[0].split('\n')
    myTicket = parsedInput[1].split('\n')[1].split(',')
    tickets = parsedInput[2].split('\n')[1:]

    _FIELDS = len(fields)
    ranges = []
  #  setForPart1 = set()
    for field in fields:
        field = field.split(':')
        name = field[0]
        field = field[1].split(' ')
        firstRange, secondRange = field[1].split('-'), field[3].split('-')
        firstRange = range(int(firstRange[0]), int(firstRange[1]) + 1)   
        secondRange = range(int(secondRange[0]), int(secondRange[1]) + 1)      
        ranges.append(set(firstRange) | set(secondRange))



    validTickets = []
    ans1 = 0         
    for ticket in tickets:
        ticket = ticket.split(',')
        if all([checkNum(num,ranges) for num in ticket ]):
            validTickets.append(ticket)
            
            #Uncomment for PART1
    #     else:     
    #         for num in ticket:
    #             if not any(int(num) in r for r in ranges):
    #                 ans1 += int(num)
    # print(ans1)

    validTickets.append(myTicket)
    possiblePositions = []
    
    for i in range(_FIELDS):
        positions = []
        for j in range(20):
            if all([int(ticket[j]) in ranges[i] for ticket in validTickets]):
                positions.append(j)
        possiblePositions.append(set(positions))

    found = 0
    USED = [False for _ in range(_FIELDS)]
    MAPPED = [None for _ in range(_FIELDS)]
    while True:
        for i in range(_FIELDS):
            valid = [j for j in possiblePositions[i] if not USED[j]]
            if len(valid) == 1:
                MAPPED[i] = valid[0]
                USED[valid[0]] = True
                found += 1
        if found == _FIELDS:
            break 

    ans2 = 1
    for num in [int(myTicket[i]) for i in MAPPED[0:6]]:
        ans2 *= num

    print(ans2)

def removeNum(possiblePositions, num):
    for pos in possiblePositions:
        pos = pos - num

def checkNum(num,ranges):
    if any([int(num) in field for field in ranges]):
        return True
    else: 
        return False
main()