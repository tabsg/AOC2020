def main():
    file1 = open('day2input.txt', 'r')
    lines = file1.readlines()
    total1 = 0
    total2 = 0
    for line in lines:
        line = line.rstrip()
        if (checkValid1(line)):
            total1 += 1
        if (checkValid2(line)):
            total2 += 1
    print("part 1: " + str(total1))
    print("part 2: " + str(total2))

def checkValid1(line):
    toks = line.split(' ')
    ranges = toks[0].split('-')
    c = (toks[1])[0]
    password = toks[2]
    min = int(ranges[0])
    max = int(ranges[1])
    appearances = 0
    for i in password:
        if (i == c):
            appearances += 1
    return (appearances <= max and appearances >= min)

def checkValid2(line):
    toks = line.split(' ')
    ranges = toks[0].split('-')
    c = (toks[1])[0]
    password = toks[2]
    pos1 = int(ranges[0]) - 1
    pos2 = int(ranges[1]) - 1

    atpos1 = password[pos1]
    atpos2 = password[pos2]

    return (atpos1 == c) != (atpos2 == c)

if __name__ == "__main__":
    main()
