def main():
    file1 = open('day3input.txt', 'r')
    lines = file1.readlines()
    lines = [l.rstrip() for l in lines]
    width = len(lines[0])
    height = len(lines)
    print("part 1: " + str(countTrees(3, 1, lines, width, height)))
    prod = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for s in slopes:
        dx, dy = s
        prod *= countTrees(dx, dy, lines, width, height)
    print("part 2: " + str(prod))

def countTrees(dx, dy, lines, width, height):
    trees = 0
    x = 0
    y = 0
    while (y < height):
        trees += checkTree(x, y, lines, width)
        x += dx
        y += dy
    return trees


def checkTree(x, y, lines, width):
    if (lines[y][x % width] == '#'):
        return 1
    else:
        return 0

if __name__ == "__main__":
    main()
