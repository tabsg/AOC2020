def main():
    file1 = open('day9input.txt', 'r')
    lines = file1.readlines()
    lines = [int(line.rstrip()) for line in lines]
    print("part 1: " + str(findBad(lines, 25)))
    print("part 2: " + str(sum(findRange(lines,findBad(lines, 25)))))

def findRange(lines, goal):
    for i in range(len(lines)):
        if lines[i] < goal:
            buf = []
            buf.append(lines[i])
            for j in range(i + 1, len(lines)):
                buf.append(lines[j])
                if sum(buf) == goal:
                    return (min(buf), max(buf))
                elif sum(buf) > goal:
                    break

def findBad(lines, bSize):
    buf = []
    for n in range(len(lines)):
        if n > 25:
            buf.pop(0)
            if not validNum(buf, lines[n]):
                return lines[n]
        buf.append(lines[n])
    return[0]

def validNum(buf, n):
    for i in range(len(buf)):
        for j in range(i + 1, len(buf)):
            if buf[i] + buf[j] == n:
                return True
    return False

if __name__ == "__main__":
    main()
