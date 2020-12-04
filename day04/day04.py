import fileinput
import re

def read_input(filename):
    passList = [] 
    passports = open(filename, "r").read().strip().split("\n\n")
    for passport in passports:
        passDict = {}
        temp = re.split(' |\n', passport)
        for field in temp:
            kv = field.split(':')
            passDict[kv[0]] = kv[1]
        passList.append(passDict)
    return passList

def main():
    passports = read_input("input4.txt")
    fields = {
        'byr': lambda x: 2002 >= int(x) >= 1920,
        'iyr': lambda x: 2020 >= int(x) >= 2010,
        'eyr': lambda x: 2030 >= int(x) >= 2020,
        'hgt': lambda x: (x[-2:] == 'cm' and 193 >= int(x[:-2]) >= 150) or (x[-2:] == 'in' and 76 >= int(x[:-2]) >= 59),
        'hcl': lambda x: x[0] == '#' and len(x) == 7 and all(char in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'] for char in x[1:]),
        'ecl': lambda x: x in ['amb','blu','brn','gry','grn','hzl','oth'],
        'pid': lambda x: len(x) == 9  and x.isdigit()
    }
    ans1 = ans2 = 0
    for passport in passports:
        if all(key in passport for key in fields):
            ans1 += 1
            if all(fields[key](passport[key]) for key in fields):
                ans2 += 1
    print(ans1, ans2)

main()