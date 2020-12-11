from collections import Counter, defaultdict

def main():
    file1 = open('day10input.txt', 'r')
    lines = [int(line.rstrip()) for line in file1.readlines()]
    lines.sort()
    lines.insert(0,0)
    lines.append(lines[len(lines)- 1] + 3)
    print("part 1: " + str(solve(lines)))
    print("part 2: " + str(solve2(lines)))

def solve(lines):
    c = Counter(j - i for i,j in zip(lines, lines[1:]))
    return c[1], c[3]

def solve2(lines):
    memo = defaultdict(int)
    device = lines.pop()
    memo[device] = 1
    print(memo)
    for i in reversed(lines):
        memo[i] = memo[i+1] + memo[i+2] + memo[i+3]
        print(memo)
        print("")
    return memo[0]

if __name__ == "__main__":
    main()
