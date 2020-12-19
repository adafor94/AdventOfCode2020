from collections import deque

def main():
    expressions = open("input18.txt", "r").read().strip().split('\n')

    sum = 0
    for expression in expressions:
        sum += int(calc2(expression))

    print(sum)

def calc(exp):
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

def calc2(exp):
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
            temp = calc2(temp)
            e += temp
        else:
            e += char
        i += 1
    return calc(e)

main()