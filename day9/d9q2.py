'''Day 9 question 1'''


def parse_data():
    '''Parse the input data'''
    res = []
    with open('data.txt') as f:
        line = f.readline()
        while line:
            data = line.split()
            res.append(data)
            line = f.readline()

    return res


move_head = {
    'R': lambda pos: (pos[0] + 1, pos[1]),
    'L': lambda pos: (pos[0] - 1, pos[1]),
    'U': lambda pos: (pos[0], pos[1] + 1),
    'D': lambda pos: (pos[0], pos[1] - 1),
}

move_tail = {
    '(-2, -2)': lambda pos: (pos[0] - 1, pos[1] - 1),
    '(-2, -1)': lambda pos: (pos[0] - 1, pos[1] - 1),
    '(-2, 0)': lambda pos: (pos[0] - 1, pos[1]),
    '(-2, 1)': lambda pos: (pos[0] - 1, pos[1] + 1),
    '(-2, 2)': lambda pos: (pos[0] - 1, pos[1] + 1),
    '(-1, -2)': lambda pos: (pos[0] - 1, pos[1] - 1),
    '(-1, 2)': lambda pos: (pos[0] - 1, pos[1] + 1),
    '(0, -2)': lambda pos: (pos[0], pos[1] - 1),
    '(0, 2)': lambda pos: (pos[0], pos[1] + 1),
    '(1, -2)': lambda pos: (pos[0] + 1, pos[1] - 1),
    '(1, 2)': lambda pos: (pos[0] + 1, pos[1] + 1),
    '(2, -2)': lambda pos: (pos[0] + 1, pos[1] - 1),
    '(2, -1)': lambda pos: (pos[0] + 1, pos[1] - 1),
    '(2, 0)': lambda pos: (pos[0] + 1, pos[1]),
    '(2, 1)': lambda pos: (pos[0] + 1, pos[1] + 1),
    '(2, 2)': lambda pos: (pos[0] + 1, pos[1] + 1),

}

history = {}


def move(head_pos, tail_pos):
    '''Move the tail to follow the head'''
    delta = (head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1])
    if abs(delta[0]) <= 1 and abs(delta[1]) <= 1:
        return tail_pos
    return(move_tail[str(delta)](tail_pos))


commands = parse_data()
head = (0, 0)
tails = [(0, 0)] * 9
history[str(tails[8])] = 1
for command in commands:
    for i in range(0, int(command[1])):
        head = move_head[command[0]](head)
        tails[0] = move(head, tails[0])
        for j in range(1, 9):
            tails[j] = move(tails[j - 1], tails[j])
        history[str(tails[8])] = 1
print(len(history))
