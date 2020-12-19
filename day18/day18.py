from collections import deque

def main():
    expressions = open("input18.txt", "r").read().strip().split('\n')

    sum = 0
    for expression in expressions:
        sum += int(simplify(expression))
    print(sum)

def calcP1(exp):
    exp = exp.split(' ')
    sum = int(exp[0])
    i = 1
    while i < len(exp):
        char = exp[i]
        if char == '+':
            sum += int(exp[i+1])
            i += 1
        if char == '*':
            sum *= int(exp[i+1])
            i += 1
        i += 1
    return str(sum)

def calcP2(exp):
    exp = exp.split(' ')
    i = 0
    while i < len(exp):
        char = exp[i]
        if char == '+':
            s = int(exp[i-1]) + int(exp[i+1])
            a = []
            if i > 2:
                a = exp[0:i-1]           
            exp =  a + [str(s)] + exp[i+2:]
            i = 0
        else:
            i += 1

    i = 0        
    while i < len(exp):
        char = exp[i]
        if char == '*':
            s = int(exp[i-1]) * int(exp[i+1])
            a = []
            if i > 2:
                a = exp[0:i-1]           
            exp =  a + [str(s)] + exp[i+2:]
            i = 0
        else:
            i += 1

    return str(exp[0])

def simplify(exp):
    stack = deque()
    e = ''
    i = 0
    while i < len(exp):
        char = exp[i]
        if char == '(':
            stack.append(i)
            temp = ''
            while stack:
                i += 1
                if exp[i] == '(':
                    stack.append(i)
                    temp += exp[i]
                elif exp[i] == ')':
                    stack.pop()
                    if stack:
                        temp += exp[i]
                else:
                    temp += exp[i]
            temp = simplify(temp)
            e += temp
        else:
            e += char
        i += 1
    return calcP1(e)   #Change to calcP1(e) for PART1

main()