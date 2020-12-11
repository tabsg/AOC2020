def main():
    file1 = open('day7input.txt', 'r')
    lines = file1.readlines()
    lines = [line.rstrip() for line in lines]
    lines = [line.split("contain") for line in lines]
    outer = [line[0].replace(" bags ","") for line in lines]
    inner = [line[1].split(",") for line in lines]
    print("part 2: " + str(part2(outer, inner)))
    inner = getColours(inner)
    colourDict = dict(zip(outer, inner))
    solution = list(dict.fromkeys(getAll(colourDict)))
    print("part 1: " + str(len(solution)))

def part2(outer, inner):
    colourDict = dict(zip(outer, getColNum(inner)))
    total = 0
    toCount = colourDict["shiny gold"]
    while len(toCount) > 0:
        colour = toCount.pop()
        if colour[0] != 'n':
            for i in range(int(colour[0])):
                toCount += colourDict[colour[1]]
                total += 1
    return total

def countChildren(colourDict, colour):
    curr = colour

def getAll(colourDict):
    toCheck, valid, checked = [], [], []
    toCheck += countColour(colourDict, "shiny gold")
    valid += countColour(colourDict, "shiny gold")
    while len(toCheck) > 0:
        colour = toCheck.pop()
        checked.append(colour)
        newPoss = countColour(colourDict, colour)
        if len(newPoss) > 0:
            valid += newPoss
            for i in newPoss:
                if not i in checked:
                    toCheck.append(i)
    return valid

def countColour(colourDict, colour):
    valid = []
    for outer in colourDict.keys():
        if colour in colourDict[outer]:
            valid.append(outer)
    return valid

def getColNum(inner):
    colnum = []
    for line in inner:
        current = []
        for bag in line:
            current.append((getNumber(bag), getColour(bag)))
        colnum.append(current)
    return colnum

def getColours(inner):
    colours = []
    for line in inner:
        current = []
        for bag in line:
            current.append(getColour(bag))
        colours.append(current)
    return colours

def getNumber(bag):
    return bag[1]

def getColour(bag):
    noNumber = bag[3:]
    colour = (noNumber.split(" bag"))
    return colour[0]

if __name__ == "__main__":
    main()
