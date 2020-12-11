def main():
    file1 = open('day1input.txt', 'r')
    lines = file1.readlines()
    numbers = []
    for line in lines:
        numbers.append(int(line.rstrip("\n")))
    (a, b) = getVals(numbers)
    print ("part 1: " + str(a * b))
    (a, b, c) = get3Vals(numbers)
    print ("part 2: " + str(a * b * c))


def getVals(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if (numbers[j] == 2020 - numbers[i]):
                return (numbers[i], numbers[j])

def get3Vals(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                if (numbers[i] + numbers[j] + numbers[k] == 2020):
                    return (numbers[i], numbers[j], numbers[k])

if __name__ == "__main__":
    main()

