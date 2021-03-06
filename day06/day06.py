import fileinput
import functools

def alternativeExplicitVersion(groups):
    ans1 = ans2 = 0
    for group in groups:
        s1 = s2 = set(group[0])

        for i in range(1,len(group)):
            s1 = s1 | set(group[i])
            s2 = s2 & set(group[i])  
        ans1 += len(s1)    
        ans2 += len(s2)
    print(ans1, ans2)

def main():
    temp = open("input6.txt", "r").read().strip().split("\n\n")
    groups = [group.split("\n") for group in temp]

    print(sum([len(functools.reduce(lambda a, b: set(a) | set(b), g)) for g in groups]))
    print(sum([len(functools.reduce(lambda a, b: set(a) & set(b), g)) for g in groups]))    

main()