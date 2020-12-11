def main():
    file1 = open('day11input.txt', 'r')
    lines = file1.readlines()
    lines = [line.rstrip() for line in lines]
    print("part 1: " + str(part1(lines)))
    print("part 2: " + str(part2(lines)))

def part2(lines):
    seats = lines
    while getNextIter2(seats) != seats:
        seats = getNextIter2(seats)
    return countOccupied(seats)

def getNextIter2(lines):
    result = []
    w = len(lines[0])
    h = len(lines)
    for y in range(h):
        result.append([])
        for x in range(w):
            filled = getNeighbours2(lines, x, y, w, h)
            if (filled == 0 and lines[y][x] == 'L'):
                result[y].append('#')
            elif (filled >= 5 and lines[y][x] == '#'):
                result[y].append('L')
            else:
                result[y].append(lines[y][x])
    return result

def getNeighbours2(lines, x, y, w, h):
    filled = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if inBounds(x, y, dx, dy, w, h) and not isCentre(dx, dy):
                if getFirstChair(lines, x, y, dx, dy, w, h) == '#':
                    filled += 1
    return filled

def getFirstChair(lines, x, y, dx, dy, w, h):
    dx1 = dx
    dy1 = dy
    while lines[y + dy][x + dx] == '.':
        if inBounds(x, y, dx + dx1, dy + dy1, w, h):
            dy += dy1
            dx += dx1
        else:
            return '.'
    return lines[y + dy][x + dx]


def part1(lines):
    seats = lines
    while getNextIter(seats) != seats:
        seats = getNextIter(seats)
    return countOccupied(seats)

def countOccupied(seats):
    filled = 0
    for y in range(len(seats)):
        for x in range(len(seats[0])):
            if seats[y][x] == '#':
                filled += 1
    return filled

def getNextIter(lines):
    result = []
    w = len(lines[0])
    h = len(lines)
    for y in range(h):
        result.append([])
        for x in range(w):
            filled = getNeighbours(lines, x, y, w, h)
            if (filled == 0 and lines[y][x] == 'L'):
                result[y].append('#')
            elif (filled >=4 and lines[y][x] == '#'):
                result[y].append('L')
            else:
                result[y].append(lines[y][x])
    return result

def getNeighbours(lines, x, y, w, h):
    filled = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if inBounds(x, y, dx, dy, w, h) and not isCentre(dx, dy):
                if lines[y + dy][x + dx] == '#':
                    filled += 1
    return filled


def inBounds(x, y, dx, dy, w, h):
    return (x + dx >= 0) and (x + dx < w) and (y + dy >= 0) and (y + dy < h)

def isCentre(dx, dy):
    return (dx == 0) and (dy == 0)

if __name__ == "__main__":
    main()
