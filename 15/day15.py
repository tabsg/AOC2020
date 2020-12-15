from collections import defaultdict

def main():
    file1 = open('day15input.txt', 'r')
    line = file1.readline()
    line = line.split(',')
    line = [int(n) for n in line]
    line1 = [int(n) for n in line]
    print("part 1:", play(2020, line))
    print("part 2:", play(30000000, line1))

def play(turns, nums):
    memory = defaultdict(lambda: turn)
    prev = -1
    for turn, n in enumerate(nums):
        memory[prev], prev = turn, n
    for turn in range(len(nums), turns):
        memory[prev], prev = turn, turn - memory[prev]
    return prev

if __name__ == "__main__":
    main()
