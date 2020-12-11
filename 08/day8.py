def main():

    file1 = open('day8input.txt','r')
    instructions = [(inst,int(value)) for inst,value in (
            tuple(line.strip().split(" ")) for line in file1.readlines())]
    (end, result) = execute(instructions)
    print("part 1: " + str(result))
    print("part 2: " + str(findFlaw(instructions)))

def execute(instructions):
    acc = 0
    i = 0
    executed = []
    while i < len(instructions):
        if i in executed:
            return ('loop',acc)
        inst,value = instructions[i]
        executed.append(i)
        if inst =='jmp':
            i += value
        else:
            if inst == 'acc':
                acc += value
            i += 1
    return ('term',acc)

def findFlaw(instructions):
    i = 0
    while True:
        oldInst = instructions[i]
        if oldInst[0] != 'acc':
            if oldInst[0] == 'jmp':
                newInst = ('nop', oldInst[1])
            else:
                newInst = ('jmp', oldInst[1])
            instructions[i] = newInst
        result = execute(instructions)
        if result[0] == 'term':
            return result[1]
        instructions[i] = oldInst
        i += 1

if __name__ == '__main__':
    main()
