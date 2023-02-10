""" Day 8 question 2 """

import functools


def build_map():
    '''Build the question map from the given input'''

    q_map = []
    with open('data.txt') as f:
        line = f.readline()
        while line:
            line = [int(x) for x in line[:-1]]
            q_map.append(line)
            line = f.readline()
    return q_map


def calc_cell_value(q_map, x, y):
    '''Calc the value for a given cell'''

    values = [0 for i in range(4)]

    # left side
    for i in range(x-1, -1, -1):
        values[0] += 1
        if q_map[y][i] >= q_map[y][x]:
            break
    # right side
    for i in range(x+1, len(q_map[0]), 1):
        values[1] += 1
        if q_map[y][i] >= q_map[y][x]:
            break
    # top side
    for i in range(y-1, -1, -1):
        values[2] += 1
        if q_map[i][x] >= q_map[y][x]:
            break
    # buttom side
    for i in range(y+1, len(q_map), 1):
        values[3] += 1
        if q_map[i][x] >= q_map[y][x]:
            break
    return functools.reduce(lambda x, y: x * y, values)


def build_cell_map(cell_map):
    '''Create a map that holds all cells values'''

    v_map = [list('0' * len(cell_map[0])) for i in range(len(cell_map))]
    for y in range(0, len(cell_map), 1):
        for x in range(0, len(cell_map[0]), 1):
            v_map[y][x] = calc_cell_value(cell_map, x, y)
    return v_map


question_map = build_map()
value_map = build_cell_map(question_map)
max_value = max([max(x) for x in value_map])
print(max_value)
