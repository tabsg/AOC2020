def main():
    file1 = open('day6input.txt', 'r')
    contents = file1.read()
    contents = contents.split("\n\n")
    print(getAny(contents))
    print(getAll(contents))

def getAny(contents):
    contents = [group.replace("\n","") for group in contents]
    contents = [nub(group) for group in contents]
    lengths = [len(group) for group in contents]
    total = sum(lengths)
    return(total)

def getAll(contents):
    contents = [group.split("\n") for group in contents]
    contents = [findAll(group) for group in contents]
    lengths = [len(group) for group in contents]
    total = sum(lengths)
    return(total)

def findAll(group):
    allqs = group[0]
    for question in group[0]:
        for person in group:
            if (not (question in person)) and question in allqs:
                allqs = allqs.replace(question,"")
    return allqs


def nub(alist):
    return list(dict.fromkeys(alist))

if __name__ == "__main__":
    main()
