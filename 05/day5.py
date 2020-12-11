def main():
    file1 = open('day5input.txt', 'r')
    lines = file1.readlines()
    lines = [l.rstrip() for l in lines]
    (seats, sids) = getInfo(lines)
    print("largest seatID: " + str(max(sids)))
    (r, c) = findMissing(seats)
    print("my seatID: " + str(getSid(r, c)))

def getSid(r, c):
    return r * 8 + c

def getInfo(lines):
    sids, seats = [], []
    for l in lines:
        row = fromBSP(l[:7])
        col = fromBSP(l[7:])
        seats.append((row, col))
        sids.append(getSid(row, col))
    return (seats, sids)


def findMissing(seats):
    maxrow = max([seat[0] for seat in seats])
    taken = [[False] * 8 for i in range(maxrow + 1)]
    for i in range(len(seats)):
        taken[seats[i][0]][seats[i][1]] = True
    looking = False
    for r in range(len(taken)):
        for c in range(len(taken[0])):
            if (not taken[r][c] and looking):
                return (r, c)
            elif (taken[r][c] and not looking):
                looking = True

def fromBSP(bsp):
    binpos = "0b"
    for c in bsp:
        if c == 'B' or c == 'R':
            binpos += '1'
        else:
            binpos += '0'
    return int(binpos, 2)

if __name__ == "__main__":
    main()
