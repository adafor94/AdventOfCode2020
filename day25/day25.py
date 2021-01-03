def main():
    cardPublicKey, doorPublicKey = 1327981, 2822615
    cardLoopSize = findLoopSize(cardPublicKey)
    doorLoopSize = findLoopSize(doorPublicKey)
    encryptionKey1 = pow(int(cardPublicKey), doorLoopSize, 20201227)
    # encryptionKey2 = pow(int(doorPublicKey), cardLoopSize, 20201227)
    
    print('PK:', cardPublicKey, doorPublicKey, 'LS:', cardLoopSize, doorLoopSize, 'EK:', encryptionKey1)

def findLoopSize(key):
    i = 0
    sum = 1
    while sum != key:
        sum = (sum*7) % 20201227
        i += 1
    return i

main()
