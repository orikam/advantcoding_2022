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
    '(-2, -1)': lambda pos: (pos[0] - 1, pos[1] - 1),
    '(-2, 0)': lambda pos: (pos[0] - 1, pos[1]),
    '(-2, 1)': lambda pos: (pos[0] - 1, pos[1] + 1),
    '(-1, -2)': lambda pos: (pos[0] - 1, pos[1] - 1),
    '(-1, 2)': lambda pos: (pos[0] - 1, pos[1] + 1),
    '(0, -2)': lambda pos: (pos[0], pos[1] - 1),
    '(0, 2)': lambda pos: (pos[0], pos[1] + 1),
    '(1, -2)': lambda pos: (pos[0] + 1, pos[1] - 1),
    '(1, 2)': lambda pos: (pos[0] + 1, pos[1] + 1),
    '(2, -1)': lambda pos: (pos[0] + 1, pos[1] - 1),
    '(2, 0)': lambda pos: (pos[0] + 1, pos[1]),
    '(2, 1)': lambda pos: (pos[0] + 1, pos[1] + 1),

}

history = {}


commands = parse_data()
head = (0, 0)
tail = (0, 0)
history[str(tail)] = 1
for command in commands:
    for i in range(0, int(command[1])):
        head = move_head[command[0]](head)
        delta = (head[0] - tail[0], head[1] - tail[1])
        if abs(delta[0]) <= 1 and abs(delta[1]) <= 1:
            continue
        tail = move_tail[str(delta)](tail)
        history[str(tail)] = 1
print(len(history))
