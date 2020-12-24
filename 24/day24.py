def main():
    file1 = open('day24input.txt', 'r')
    lines = [line.rstrip() for line in file1.readlines()]
    coords = getCoords(lines)
    black = getTiles(coords)
    print("part 1:", len(black))
    print("part 2:", playDays(black))

def playDays(black):
    for _ in range(100):
        toCheck = set()
        black2 = set()
        black, black2, toCheck = iterateBlack(black, black2, toCheck)
        black, toCheck = checkWhite(black, black2, toCheck)
    return len(black)

def iterateBlack(black, black2, toCheck):
    adjacent = [(1,1), (2,0), (1,-1), (-1,-1), (-2,0), (-1,1)]
    for x, y in black:
        count = 0
        for dx, dy in adjacent:
            if (x + dx, y + dy) in black:
                count += 1
            else:
                toCheck.add((x + dx, y + dy))
        if 1 <= count <= 2:
            black2.add((x, y))
    return black, black2, toCheck

def checkWhite(black, black2, toCheck):
    adjacent = [(1,1), (2,0), (1,-1), (-1,-1), (-2,0), (-1,1)]
    for x, y in toCheck:
        count = 0
        for dx, dy in adjacent:
            if (x + dx, y + dy) in black:
                count += 1
        if count == 2:
            black2.add((x, y))
    black = black2
    return black, toCheck

def getTiles(coords):
    black = set()
    for coord in coords:
        x, y = getTile(coord)
        if (x, y) in black:
            black.remove((x, y))
        else:
            black.add((x, y))
    return black

def getTile(coord):
    x = sum([step[0] for step in coord])
    y = sum([step[1] for step in coord])
    return (x, y)


def getCoords(lines):
    coords = []
    for line in lines:
        coords.append(translate(line))
    return coords

def translate(line):
    coord = []
    i = 0
    while i < len(line):
        if line[i] == 'n' and line[i + 1] == 'e':
            coord.append((1,1))
            i += 2
        elif line[i] == 'n' and line[i + 1] == 'w':
            coord.append((-1,1))
            i += 2
        elif line[i] == 's' and line[i + 1] == 'e':
            coord.append((1, -1))
            i += 2
        elif line[i] == 's' and line[i + 1] == 'w':
            coord.append((-1, -1))
            i += 2
        elif line[i] == 'e':
            coord.append((2, 0))
            i += 1
        else:
            coord.append((-2, 0))
            i += 1
    return coord


if __name__ == "__main__":
    main()
