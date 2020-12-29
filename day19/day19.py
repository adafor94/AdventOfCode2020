def main():
    input = open("input19.txt", "r").read().strip().split('\n\n')
    rules = input[0].split('\n')
    messages = input[1].split('\n')

    r = {}

    for rule in rules: 
        rule = rule.split(':')
        num = rule[0]

        if rule[1].strip()[0] == '"':
            char = rule[1].strip()[1]
            func = returnLambda(char)
            r[num] = SimpleParser(r, func)
        else:
            rules = [subrule.strip().split(' ') for subrule in rule[1].split('|')]
            r[num] = Parser(r,rules)
        
        #Uncomment for PART2
        # if num == '8':
        #     r[num] = Parser(r, [['42'], ['42', '8']])
        # elif num == '11':
        #     r[num] = Parser(r, [['42', '31'], ['42', '11', '31']])

    ans1 = 0
    for mess in messages:
        result = r['0'].parse([(True, mess)], 0, len(mess))
        if any([m == (True, '') for m in result]):
            ans1 += 1
    print(ans1)

def returnLambda(char):
    return lambda x: (char == x[0], x[1:]) if len(x) > 0 else (False, 'LAMBDAFAIL')

class SimpleParser():       #Parses a single message returning parsed message or fail.
    def __init__(self, r, func):
        self.r = r
        self.func = func

    def parse(self, messages, count, limit):
        validMessages = []
        for m in messages:
            parsedMessage = self.func(m[1])
            if parsedMessage[0]:
                validMessages.append(parsedMessage)
  #     print(message, parsedMessage)
    
        return validMessages

class Parser():
    def __init__(self, r, rules):
        self.r = r
        self.rules = rules

    def parse(self, messages, count, limit):
        count += 1
        validMessages = []
        if count > limit:
            return validMessages

 #       print(self.rules)
        for rule in self.rules:
#            print(rule) 
            temp = messages
            for num in rule:
         #       print(num)
                temp = self.r[num].parse(temp, count, limit)
            validMessages += temp
        return validMessages    
main()

    
