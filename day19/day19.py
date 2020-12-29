def main():
    input = open("input19.txt", "r").read().strip().split('\n\n')
    allRules = input[0].split('\n')
    messages = input[1].split('\n')
    r = {}

    parsers = 0
    for rule in allRules: 
        rule = rule.split(':')
        num = rule[0]

        if rule[1].strip()[0] == '"':
            char = rule[1].strip()[1]
            func = returnLambda(char)
            r[num] = SimpleParser(r, func)
        else:
            rules = [subrule.strip().split(' ') for subrule in rule[1].split('|')]
            r[num] = Parser(r,rules)
            parsers += 1
        
    #Uncomment for PART2
    # r['8'] = Parser(r, [['42'], ['42', '8']])
    # r['11'] = Parser(r, [['42', '31'], ['42', '11', '31']])

    ans1 = 0
    for mess in messages:
        result = r['0'].parse([(True, mess)], 0, len(allRules))
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
        for rule in self.rules:
            temp = messages
            for num in rule:
                temp = self.r[num].parse(temp, count, limit)
            validMessages += temp
        return validMessages    
main()

    
