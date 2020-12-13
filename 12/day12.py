def main():
    file1 = open('day12input.txt', 'r')
    lines = file1.readlines()
    instr = getInstructions(lines)
    (x, y, cdir) = solve1(instr, (0, 0, 1))
    print("part 1:", abs(x) + abs(y))
    nship, nwp = solve2(instr, (0, 0), (10, 1))
    (wx, wy) = nship
    print("part 2:", abs(wx) + abs(wy))

def getInstructions(lines):
    lines = [line.rstrip() for line in lines]
    dirs = [line[0] for line in lines]
    vals = [int(line[1:]) for line in lines]
    instr = list(zip(dirs, vals))
    return instr

def solve2(instr, ship, wp):
    for i in instr:
        (ship, wp) = execute2(i, ship, wp)
    return (ship, wp)

def execute2(ins, ship, wp):
    if ins[0] in "NSEW":
        return wdirec(ins, ship, wp)
    if ins[0] in "LR":
        return wrot(ins, ship, wp)
    return wforw(ins[1], ship, wp)


def wdirec(ins, ship, wp):
    (x, y) = wp
    if ins[0] == 'N' or ins[0] == 0:
        return (ship, (x, y + ins[1]))
    if ins[0] == 'S' or ins[0] == 2:
        return (ship, (x, y - ins[1]))
    if ins[0] == 'E' or ins[0] == 1:
        return (ship, (x + ins[1], y))
    return (ship, (x - ins[1], y))

def wrot(ins, ship, wp):
    for i in range(int((ins[1] / 90))):
        if ins[0] == 'L':
            wp = wrot1L(wp)
        else:
            wp = wrot1R(wp)
    return (ship, wp)

def wforw(ins, ship, wp):
    (wx, wy) = wp
    (x, y) = ship
    ship = (x + ins * wx, y + ins * wy)
    return (ship, wp)

def wrot1L(wp):
    (x, y) = wp
    return (-y, x)

def wrot1R(wp):
    (x, y) = wp
    return (y, -x)

def solve1(instr, ship):
    for i in instr:
        ship = execute(i, ship)
    return ship

def execute(ins, ship):
    if ins[0] in "NSEW":
        return direc(ins, ship)
    if ins[0] in "LR":
        return rot(ins, ship)
    return forw(ins[1], ship)

def direc(ins, ship):
    (x, y, cdir) = ship
    if ins[0] == 'N' or ins[0] == 0:
        return (x, y + ins[1], cdir)
    if ins[0] == 'S' or ins[0] == 2:
        return (x, y - ins[1], cdir)
    if ins[0] == 'E' or ins[0] == 1:
        return (x + ins[1], y, cdir)
    return (x - ins[1], y, cdir)

def rot(ins, ship):
    (x, y, cdir) = ship
    if ins[0] == 'L':
        return (x, y, (cdir - (ins[1] / 90)) % 4)
    return (x, y, (cdir + (ins[1] / 90)) % 4)

def forw(val, ship):
    (x, y, cdir) = ship
    return direc((cdir, val), ship)

if __name__ == "__main__":
    main()
