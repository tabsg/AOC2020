def main():
    file1 = open('day13input.txt', 'r')
    lines = file1.readlines()
    early = int(lines[0])
    buses = (lines[1].split(","))
    print("part 1: " + str(part1(early, buses)))
    print("part 2: " + str(part2(buses)))


def part2(buses):
    buses = [(i, int(bus_id)) for i, bus_id in enumerate(buses) if bus_id != 'x']
    jump = buses[0][1]
    time = 0
    for diff, bus in buses[1:]:
        while (time + diff) % bus != 0:
            time += jump
        jump *= bus
    return time

def part1(early, buses):
    buses = [int(bus) for bus in buses if bus != "x"]
    times = [first(early, bus) for bus in buses]
    (time, bus) = min(times, key = lambda t: t[0])
    return (time * bus)


def first(early, bus):
    prev = early // bus
    wait = ((prev + 1) * bus) - early
    return (wait, bus)

if __name__ == "__main__":
    main()
