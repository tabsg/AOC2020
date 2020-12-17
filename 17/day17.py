import copy

def main():
    print(part1())
    print(part2())

def part2():
    active = initActive()
    for _ in range(6):
        toCheck = set()
        nActive = set()
        active, nActive, toCheck = iterateActive(active, nActive, toCheck)
        active, toCheck = checkInactive(active, nActive, toCheck)
    return len(active)

def initActive():
    active = set()
    file2 = open('day17input.txt', 'r')
    for x, line in enumerate(file2.readlines()):
        for y, field in enumerate(line.strip()):
            if field == '#':
                active.add((x, y, 0, 0))
    return active


def iterateActive(active, nActive, toCheck):
    for x, y, z, w in active:
        count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    for dw in range(-1, 2):
                        if (x + dx, y + dy, z + dz, w + dw) in active:
                            count += 1
                        else:
                            toCheck.add((x + dx, y + dy, z + dz, w + dw))
        if 3 <= count <= 4: #including active centre
            nActive.add((x, y, z, w))
    return active, nActive, toCheck

def checkInactive(active, nActive, toCheck):
    for x, y, z, w in toCheck:
        count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    for dw in range(-1, 2):
                        if (x + dx, y + dy, z + dz, w + dw) in active:
                            count += 1
        if count == 3:
            nActive.add((x, y, z, w))
    active = nActive
    return active, toCheck

def part1():
    file1 = open('day17input.txt', 'r')
    cube = [[line.rstrip() for line in file1.readlines()]]
    for _ in range(6):
        cube, tActive = calcNext(cube)
    return tActive

def calcNext(cube):
    cube = expandCube(cube)
    w, h, d = len(cube[0][0]), len(cube[0]), len(cube)
    res = copy.deepcopy(cube)
    tActive = 0
    for z in range(len(cube)):
        for y in range(len(cube[z])):
            res[z][y] = ''
            for x in range(len(cube[z][y])):
                current = point(x, y, z, cube)
                active = checkNeighbours(x, y, z, w, h, d, cube)
                if current == '#' and not (active == 2 or active == 3):
                    res[z][y] += '.'
                elif current == '.' and active == 3:
                    res[z][y] += '#'
                else:
                    res[z][y] += current
            tActive += res[z][y].count('#')
    return res, tActive

def checkNeighbours(x, y, z, w, h, d, cube):
    total = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if inBounds(x, dx, y, dy, z, dz, w, h, d):
                    if point(x + dx, y + dy, z + dz, cube) == '#':
                        total += 1
    return total

def point(x, y, z, cube):
    return cube[z][y][x]

def inBounds(x, dx, y, dy, z, dz, w, h, d):
    inRange = 0 <= x + dx < w and 0 <= y + dy < h and 0 <= z + dz < d
    isCentre = dx == 0 and dy == 0 and dz == 0
    return inRange and not isCentre

def expandCube(cube):
    cSize = len(cube[0]) + 2
    cube = [expandFace(face, cSize) for face in cube]
    cube = addLayers(cube, cSize)
    return cube

def addLayers(cube, cSize):
    blankFace = [('.' * cSize) for _ in range(cSize)]
    cube.insert(0, blankFace)
    cube.append(blankFace)
    return cube

def expandFace(face, cSize):
    face = [extend(line) for line in face]
    face.insert(0, '.' * cSize)
    face.append('.' * cSize)
    return face

def extend(line):
    return '.' + line + '.'

if __name__ == "__main__":
    main()
