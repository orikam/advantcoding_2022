
ROCK = 0
PAPER = 1
SCISSORS = 3
type_score = [1, 2, 3]

LOST = 0
DRAW = 1
WON = 2
win_score = [0, 3, 6]

hands = {'A' : 0, 'B' : 1, 'C' : 2, 'X' : 0, 'Y' : 1, 'Z' : 2}
win_values = [-2, 1]
win_hands = {'A': 'Y', 'B': 'Z', 'C': 'X'}
lose_hands = {'A': 'Z', 'B': 'X', 'C': 'Y'}
def win(you, me):
    if you == me:
        return 3
    if (me - you) in win_values:
        return 6
    return 0

with open('day_2\data.txt') as f:
    line = f.readline()
    score = 0
    card = 0
    while line:
        cards = line.split()
        print(cards[0])
        if cards[1] == 'X':
            cards[1] = lose_hands[cards[0]]
        elif cards[1] == 'Y':
            cards[1] = cards[0]
        elif cards[1] == 'Z':
            cards[1] = win_hands[cards[0]]
        score += win(hands[cards[0]], hands[cards[1]])
        score += type_score[hands[cards[1]]]
        line = f.readline()
   
    #print(f'{l.index(m)} - {m}')
    print(f'total {score}')