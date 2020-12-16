def main():
    parsedInput = open("input16.txt", "r").read().strip().split('\n\n')
    fields = parsedInput[0].split('\n')
    myTicket = parsedInput[1].split('\n')[1]
    tickets = parsedInput[2].split('\n')[1:]

    ranges = set()
    for field in fields:
        field = field.split(':')
        name = field[0]
        field = field[1].split(' ')
        firstRange, secondRange = field[1].split('-'), field[3].split('-')
        firstRange = range(int(firstRange[0]), int(firstRange[1]) + 1)   
        secondRange = range(int(secondRange[0]), int(secondRange[1]) + 1)      
   
        ranges = ranges | set(firstRange) | set(secondRange)

  #  ans1 = 0
    validTickets = []
    for ticket in tickets:
        ticket = ticket.split(',')
        if all([num in ranges for num in ticket]):
            validTickets.append(ticket)
            
            #Uncomment for PART1
  #      else:              
  #          for num in ticket:
  #              if int(num) not in ranges:
  #                 ans1 += int(num)

  #  print(ans1)
main()