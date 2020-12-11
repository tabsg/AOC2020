def main():
    file1 = open('day4input.txt', 'r')
    lines = file1.readlines()
    lines = [l.rstrip() for l in lines]
    lines = concatenate(lines)
    passports = buildPassports(lines)
    (valid1, valid2) = countValid(passports)
    print(valid1)
    print(valid2)

def countValid(passports):
    valid = (0, 0)
    for p in passports:
        valid = incrementTotals(valid, checkValidity(p))
    return valid

def incrementTotals(totals, current):
    (valid1, valid2), (v1, v2) = totals, current
    valid1 += int(v1)
    valid2 += int(v2)
    return(valid1, valid2)


def checkValidity(p):
    valid1, valid2 = False, False
    if (len(p) == 8 or onlyMissingCID(p)):
        valid1 = True
        valid2 = checkValid2(p)
    return (valid1, valid2)

def buildPassports(lines):
    passports = []
    for i in range(len(lines)):
        passports.append([])
        passports[i] = lines[i].split(' ')
        passports[i].pop()
    return passports


def concatenate(lines):
    result = []
    store = ""
    for i in lines:
        if (i == ''):
            result.append(store)
            store = ""
        else:
            store += (i + ' ')
    result.append(store)
    return result

def onlyMissingCID(passport):
    if (len(passport) != 7):
        return False
    for entry in passport:
        if (entry[:3] == "cid"):
            return False
    return True

def checkValid2(passport):
    switcher ={
            "byr" : byr,
            "iyr" : iyr,
            "eyr" : eyr,
            "hgt" : hgt,
            "hcl" : hcl,
            "ecl" : ecl,
            "pid" : pid,
            "cid" : cid
    }
    for entry in passport:
        field = entry[:3]
        value = entry [4:]
        func = switcher.get(field)
        if (not func(value)):
            return False
    return True

def byr(val):
    return (int(val) >= 1920 and int(val) <= 2002)

def iyr(val):
    return (int(val) >= 2010 and int(val) <= 2020)

def eyr(val):
    return (int(val) >= 2020 and int(val) <= 2030)

def hgt(val):
    if val[-2:] == "cm":
        return (int(val[:-2]) >= 150 and int(val[:-2]) <= 193)
    elif val[-2:] == "in":
        return (int(val[:-2]) >= 59 and int(val[:-2]) <= 76)
    else:
        return False

def hcl(val):
    if val[0] != '#':
        return False
    val = val[1:]
    for i in range(len(val)):
        if not isHexDigit(val[i]):
            return False
    return True

def isHexDigit(c):
    return (c >= 'a' and c <= 'f') or (c >= '0' and c <= '9')

def ecl(val):
    return (val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])

def pid(val):
    if len(val) != 9:
        return False
    return (int(val) >= 0 and int(val) <= 999999999)

def cid(val):
    return True

if __name__ == "__main__":
    main()
