import math

def main():
    input = open("test.txt", "r").read().strip().split("\n") 
    time = int(input[0])
    ids = input[1].split(',')

    #PART 1
    idWithLowestWait = 0
    minWait = time

    for id in ids: 
        if id != 'x':
            id = int(id)
            wait = id - (time%id)
            if wait < minWait:
                minWait = wait
                idWithLowestWait = id
    print(idWithLowestWait * minWait)
    
    #PART 2
    idAndDeparture = []
    for i in range(len(ids)):
        if ids[i] != 'x':
            idAndDeparture.append([ids[i],i])

    minValue = 0
    product = 1
    for id, delay in idAndDeparture:
        id = int(id)
        delay = int(delay)
        while ((minValue+delay)%id) != 0:
            minValue += product
        product *= id
    print(minValue)

main()