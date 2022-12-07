from os import path

def score(me, opponent):
    return 3 * ((me - opponent + 1) % 3) + me + 1


with open(path.join(path.dirname(__file__), "day2.txt")) as f:
    score1, score2 = 0, 0

    for line in f.read().splitlines():
        opponent, me = map(ord, line.split())
        opponent -= ord("A")
        me -= ord("X")

        score1 += score(me, opponent)
        score2 += score((opponent + me - 1) % 3, opponent)
    
print("Part 1:", score1)
print("Part 2:", score2)