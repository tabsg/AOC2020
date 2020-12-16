import math

def main():
    with open("day16input.txt") as f:
        fields, mine, near = f.read().split('\n\n')
    fields = {f[0]: f[1] for f in (getField(f) for f in fields.splitlines())}
    mine = getMine(mine.splitlines()[1])
    near = [getMine(t) for t in near.splitlines()[1:]]
    print("part 1:", part1(fields, mine, near))
    print("part 2:", part2(fields, mine, near))

def getField(field):
    name, valid = field.split(':')
    valid = [tuple(map(int, r)) for r in
             (r.split('-') for r in valid.split(' or '))]
    return name, valid


def getMine(mine):
    return list(map(int, mine.split(',')))

def isValid(fields, value):
    return any(r[0] <= value <= r[1] for v in fields.values() for r in v)


def part1(fields, mine, near):
    return sum(n for t in near for n in t if not isValid(fields, n))


def part2(fields, mine, near):
    valid = [t for t in near if all(isValid(fields, n) for n in t)]
    candidates = {}
    for i in range(len(mine)):
        candidates[i] = set()
        for f, v in fields.items():
            if all(any(r[0] <= t[i] <= r[1] for r in v) for t in valid):
                candidates[i].add(f)
    names = {}
    while candidates:
        i = next(i for i, s in candidates.items() if len(s) == 1)
        names[i] = next(iter(candidates[i]))
        del candidates[i]
        for j in candidates:
            candidates[j].discard(names[i])

    return math.prod(n for i, n in enumerate(mine)
                     if names[i].startswith('departure'))

if __name__ == "__main__":
    main()
