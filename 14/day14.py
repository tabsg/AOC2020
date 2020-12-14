from collections import defaultdict

def main():
    file1 = open('day14input.txt', 'r')
    lines = file1.readlines()
    lines = getInput(lines)
    memory = defaultdict(int)
    memory = calc(lines, memory)
    print("part 1:", sum(memory.values()))
    memory2 = defaultdict(int)
    memory2 = calc2(lines, memory2)
    print("part 2:", sum(memory2.values()))

def calc2(lines, memory):
    mask = 0
    for line in lines:
        if line[0] == 'mask':
            mask = line[1]
        else:
            add = applyMask2(int(line[1]), mask)
            memory = doMask(add, line[2], memory)
    return memory

def doMask(add, val, memory):
    adds = genAdds(add, val, memory)
    for a in adds:
        memory[a] = val
    return memory

def genAdds(add, val, memory):
    n = add.count('X')
    add = add.split('X')
    bins = getBins(n)
    adds = []
    for b in bins:
        a = add + list(b)
        a[::2] = add
        a[1::2] = list(b)
        a = ''.join(a)
        adds.append(a)
    return adds

def getBins(n):
    bins = []
    for i in range(2**n):
        bins.append((str(bin(i))[2:]).zfill(n))
    return bins

def applyMask2(val, mask):
    output = ""
    val = (str(bin(val))[2:]).zfill(36)
    for i in range(len(mask)):
        if mask[i] == '0':
            output += val[i]
        else:
            output += mask[i]
    return output

def calc(lines, memory):
    mask = 0
    for line in lines:
        if line[0] == 'mask':
            mask = line[1]
        else:
            memory[line[1]] = applyMask(line[2],mask)
    return memory



def applyMask(val, mask):
    output = ""
    val = (str(bin(val))[2:]).zfill(36)
    for i in range(len(mask)):
        if mask[i] == 'X':
            output += val[i]
        else:
            output += mask[i]
    return int(output, 2)

def getInput(lines):
    lines = [line.rstrip() for line in lines]
    lines = [line.split(' = ') for line in lines]
    result = []
    i = 0
    for line in lines:
        result.append([])
        if "mem" in line[0]:
            result[i].append("mem")
            result[i].append(line[0][4:-1])
            result[i].append(int(line[1]))
        else:
            result[i].append("mask")
            result[i].append(line[1])
        i += 1
    return result

if __name__ == "__main__":
    main()
