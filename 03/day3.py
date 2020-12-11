def main():
    file1 = open('day3input.txt', 'r')
    lines = file1.readlines()
    lines = [l.rstrip() for l in lines]
    width = len(lines[0])
    height = len(lines)
    prod = 1
    prod *= countTrees(1, 1, lines, width, height)
    prod *= countTrees(3, 1, lines, width, height)
    prod *= countTrees(5, 1, lines, width, height)
    prod *= countTrees(7, 1, lines, width, height)
    prod *= countTrees(1, 2, lines, width, height)
    print(prod)

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
