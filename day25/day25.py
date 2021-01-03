def main():
    publicKeys = open("input25.txt", "r").read().strip().split('\n')
    cardPublicKey, doorPublicKey = publicKeys[0], publicKeys[1]
    cardLoopSize, doorLoopSize = findLoopSize(cardPublicKey), findLoopSize(doorPublicKey)
    ek1, ek2 = calcEncyptionKey(cardPublicKey, doorLoopSize), calcEncyptionKey(doorPublicKey, cardLoopSize)
    
    print('PK:', cardPublicKey, doorPublicKey, 'LS:', cardLoopSize, doorLoopSize, 'EK:', ek1, ek2)

def findLoopSize(key):
    i = 0
    sum = 1
    while True:
        if sum == int(key):
            return i
        sum = (sum*7) % 20201227
        i += 1

def calcEncyptionKey(key, loopSize):
    sum = 1
    for _ in range(loopSize):
        sum = (sum * int(key)) % 20201227   
    return sum

main()
