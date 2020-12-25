def main():
    file1 = open('day25input.txt', 'r')
    lines = file1.readlines()
    lines = [line.rstrip() for line in lines]
    door = int(lines[0])
    card = int(lines[1])
    m = 20201227
    loops = getLoops(card, m)
    ans = transform(door, loops, m)
    print("part 1:", ans)

def transform(pub, key, m):
    return modPow(pub, key, m)

def getLoops(pub, m):
    count = 0
    n = 1
    while n != pub:
        n *= 7
        n %= m
        count += 1
    return count

def modPow(a, k, m):
    if m == 1:
        return 0
    if k ==0:
        return 1
    j = k // 2
    x = (a ** 2) % m
    if k % 2 == 0:
        return modPow(x, j, m)
    return ((a % m) * modPow(x, j, m)) % m


if __name__ == "__main__":
    main()
