from collections import deque

def main():
    file1 = open('day18input.txt', 'r')
    lines = [(line.rstrip()).replace(' ','') for line in file1.readlines()]
    print("part 1:", part1(lines))
    print("part 2:", part2(lines))

def part2(lines):
    total = 0
    for line in lines:
        total += int(evalPostfix(shuntingYard2(line)))
    return total

def part1(lines):
    total = 0
    for line in lines:
        total += int(evalPostfix(shuntingYard(line)))
    return total

def shuntingYard2(line):
    postfix = []
    ops = deque()
    for symbol in line:
        if symbol.isnumeric():
            postfix.append(symbol)
        elif symbol == '+':
            ops.append(symbol)
        elif symbol == '*':
            while ops:
                if ops[-1] != '(':
                    postfix.append(ops.pop())
                else:
                    break
            ops.append(symbol)
        elif symbol == '(':
            ops.append(symbol)
        elif symbol == ')':
            op = ops.pop()
            while op != '(':
                postfix.append(op)
                op = ops.pop()
    while ops:
        postfix.append(ops.pop())
    return postfix


def evalPostfix(postfix):
    stack = deque()
    for symbol in postfix:
        if symbol.isnumeric():
            stack.append(symbol)
        elif symbol == '+':
            stack.append(int(stack.pop()) + int(stack.pop()))
        else:
            stack.append(int(stack.pop()) * int(stack.pop()))
    return stack.pop()

def shuntingYard(line):
    postfix = []
    ops = deque()
    for symbol in line:
        if symbol.isnumeric():
            postfix.append(symbol)
        elif symbol == '+' or symbol == '*':
            while ops:
                if ops[-1] != '(':
                    postfix.append(ops.pop())
                else:
                    break
            ops.append(symbol)
        elif symbol == '(':
            ops.append(symbol)
        elif symbol == ')':
            op = ops.pop()
            while op != '(':
                postfix.append(op)
                op = ops.pop()
    while ops:
        postfix.append(ops.pop())
    return postfix

if __name__ == "__main__":
    main()
