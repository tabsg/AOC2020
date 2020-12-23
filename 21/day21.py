from collections import defaultdict

def main():
    file1 = open('day21input.txt', 'r')
    labels = [e.replace(")","").split(" (contains ") for e in file1.read().split("\n")]
    labels.pop()
    allergens = getAllergens(labels)
    occurrences = getOccurences(labels)
    count = countImpossible(allergens, occurrences)
    ingredients = getIngredients(allergens)
    print("part 1:", count)
    print("part 2:", ingredients)

def getIngredients(allergens):
    used = set()
    while any(len(allergen) > 1 for allergen in allergens.values()):
        for allergen, ingredient in allergens.items():
            if len(ingredient) == 1 and ingredient[0] not in used:
                used.add(ingredient[0])
            elif len(ingredient) > 1:
                for i in used:
                    if i in ingredient:
                        allergens[allergen].remove(i)
    return ','.join(v[0] for k, v in sorted(allergens.items(), key = lambda k : k[0]))

def countImpossible(allergens, occurrences):
    count = 0
    for ingredient, freq in occurrences.items():
        if all(ingredient not in val for val in allergens.values()):
            count += freq
    return count

def getAllergens(labels):
    allergens = dict()
    for label in labels:
        for allergen in label[1].split(', '):
            if allergen in allergens:
                allergens[allergen] = [i for i in label[0].split(' ') if i in allergens[allergen]]
            else:
                allergens[allergen] = [i for i in label[0].split(' ')]
    return allergens

def getOccurences(labels):
    occurrences = defaultdict(int)
    for label in labels:
        for ingredient in label[0].split(' '):
            occurrences[ingredient] += 1
    return occurrences

if __name__ == "__main__":
    main()




