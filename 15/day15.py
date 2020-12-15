from collections import defaultdict

def main():
    file1 = open('day15input.txt', 'r')
    line = file1.readline()
    line = line.split(',')
    line = [int(n) for n in line]
    line1 = [int(n) for n in line]
    print("part 1:", play1(2020, line))
    print("part 2:", play2(30000000, line1))

def play2(turns, nums):
    memory = {n: [turn + 1] for turn, n in enumerate(nums)}
    prev = nums[-1]
    for i in range(len(memory) + 1, turns + 1):
        if len(memory[prev]) == 1:
            prev = 0
        else:
            prev = memory[prev][-1] - memory[prev][-2]
        if len(memory.get(prev, [])) == 0:
            memory[prev] = [i]
        else:
            memory[prev] = [memory[prev][-1]] + [i]
    return prev

def play1(turns, nums):
    t = 0
    memory = defaultdict(int)
    for n in nums:
        t += 1
        memory[n] = t
    prev = nums[-1]
    while t < turns:
        t += 1
        if nums.count(prev) == 1:
            curr = 0
            nums.append(curr)
            memory[prev] = t - 1
            prev = 0
        else:
            curr = t - 1 - memory[prev]
            memory[prev] = t - 1
            nums.append(curr)
            prev = curr
    return curr

if __name__ == "__main__":
    main()
