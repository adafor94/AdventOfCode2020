import fileinput

def read_input(filename):
    myFile = open(filename, "r")
    myLine = myFile.readline()
    listOfAllPassports = []
    while myLine:
        currentPassport = {}
        while myLine and myLine != "\n":
            temp = myLine.split(" ")
            for field in temp:
                temp = field.strip().split(':')
                currentPassport[temp[0]] = temp[1]
            myLine = myFile.readline()
        myLine = myFile.readline()
        listOfAllPassports.append(currentPassport)

    return listOfAllPassports
        
    myFile.close()

def main():
    passports = read_input("/home/adam/Documents/AdventOfCode2020/day04/input4.txt")
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