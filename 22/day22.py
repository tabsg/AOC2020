import copy

def main():
    file1 = open('day22input.txt', 'r')
    lines = file1.read()
    lines = lines.split("\n\n")
    lines = [line.split("\n") for line in lines]
    lines = [line[1:] for line in lines]
    player1, player2 = lines[0], lines[1]
    player2.pop()
    player1 = [int(n) for n in player1]
    p1 = copy.deepcopy(player1)
    player2 = [int(n) for n in player2]
    p2 = copy.deepcopy(player2)
    winner = playGame(player1, player2)
    print("part 1:", countScore(winner))
    print("part 2:", part2(p1, p2))

def part2(p1, p2):
    def playGame2(p1, p2):
        p1Decks, p2Decks = set(), set()
        while p1 and p2:
            deck1, deck2 = tuple(p1), tuple(p2)
            if deck1 in p1Decks or deck2 in p2Decks:
                return 0
            p1Decks.add(deck1)
            p2Decks.add(deck2)
            if len(p1) > p1[0] and len(p2) > p2[0]:
                winner = playGame2(p1[1:p1[0] + 1], p2[1:p2[0] + 1])
            else:
                winner = p2[0] > p1[0]
            winner, loser = (p1, p2)[winner], (p1, p2)[not winner]
            winner += [winner.pop(0), loser.pop(0)]
        return [p1, p2].index(winner)

    playGame2(p1, p2)
    return sum((i + 1) * c for i, c in enumerate(reversed(p1 or p2)))

def countScore(winner):
    score = 0
    for i in range(len(winner)):
        score += int(winner[::-1][i]) * (i + 1)
    return score

def playGame(p1, p2):
    p1, p2 = copy.deepcopy(p1), copy.deepcopy(p2)
    while p1 and p2:
        p1, p2 = playTurn(p1, p2)
    if p1:
        return p1
    else:
        return p2

def playTurn(p1, p2):
    c1, c2 = p1.pop(0), p2.pop(0)
    if (c1) > (c2):
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c2)
        p2.append(c1)
    return p1, p2

if __name__ == "__main__":
    main()
