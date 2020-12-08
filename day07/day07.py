import fileinput

def formatRule(rule):
    rule = rule.split("contain")
    rule1 = rule[0].strip().split(' ')
    rule1 = rule1[0] + " " + rule1[1]
    rule2 = rule[1].split(',')
    listOfFormattedRule2 = []
    for r in rule2:
        if r.strip() != 'no other bags.':
            r = r.strip().split(' ')[0:3]
            r = [r[0],r[1] + " " + r[2]]
            listOfFormattedRule2.append(r)
    return [rule1, listOfFormattedRule2]

def main():
    listOfRules = open("input7.txt", "r").read().strip().split("\n")
    listOfRules = [formatRule(rule) for rule in listOfRules]

    tree1 = {}
    tree2 = {}
    for rule in listOfRules:
        parents = rule[1]
        for parent in parents:
            if parent[1] in tree1:
                tree1[parent[1]].append(rule[0])
            else:
                tree1[parent[1]] = [rule[0]]
        tree2[rule[0]] = rule[1]

    uniqueChildren = set(listAllChildren('shiny gold', tree1))
    print(len(uniqueChildren))
    print(countProductIncludingHeadOfTree('shiny gold', tree2) - 1)

def countProductIncludingHeadOfTree(node, tree):
    bags = 0
    if node not in tree:
        return 1
    for times, child in tree[node]:
            bags +=  int(times) * int(countProductIncludingHeadOfTree(child,tree))
    return(bags + 1)

def listAllChildren(node, tree):
    nodes = []
    if node in tree:
        nodes += tree[node]
        for child in tree[node]:
            nodes += listAllChildren(child, tree)
    return(nodes)

main()