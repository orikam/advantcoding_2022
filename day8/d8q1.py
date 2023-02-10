""" Day 8 question 1 """

def build_map():
    '''Build the basic map from the given input'''
    game_map = []
    with open('data.txt') as f:
        line = f.readline()
        line = line[:-1]
        line = [int(x) for x in line]
        while line:
            game_map.append(list(line))
            line = f.readline()
            line = line[:-1]
            line = [int(x) for x in line]
    return (game_map, len(game_map), len(game_map[0]))


def build_visable_map_left(map):
    '''Build the visable left map'''
    v_map = []
    for j in range(len(map)):
        max = -1
        raw = []
        for i in range(len(map[0])):
            if map[j][i] > max:
                max = map[j][i]
                raw.append(1)
            else:
                raw.append(0)
        v_map.append(raw)
    return v_map


def build_visable_map_right(in_map):
    v_map = []
    for j in range(len(in_map)):
        max_value = -1
        raw = []
        for i in range(len(in_map[0])-1, -1, -1):
            if in_map[j][i] > max_value:
                max_value = in_map[j][i]
                raw.insert(0, 1)
            else:
                raw.insert(0, 0)
        v_map.append(raw)
    return v_map


def build_visable_map_top(map):
    v_map = []
    for i in range(len(map[0])):
        col = []
        v_map.append(col)
    for i in range(len(map[0])):
        max = -1
        for j in range(len(map)):
            if map[j][i] > max:
                max = map[j][i]
                v_map[j].append(1)
            else:
                v_map[j].append(0)
    return v_map


def build_visable_map_buttom(map):
    v_map = []
    for i in range(len(map[0])):
        col = []
        v_map.append(col)
    for i in range(len(map[0])):
        max = -1
        for j in range(len(map) - 1, -1, -1):
            if map[j][i] > max:
                max = map[j][i]
                v_map[j].append(1)
            else:
                v_map[j].append(0)
    return v_map


def count_visable(maps):
    count = 0
    map = maps[0]
    res = []
    for j in range(len(map)):
        raw = []
        for i in range(len(map[0])):
            sum = 0
            for m in maps:
                sum += m[j][i]
            if sum > 0:
                count += 1
                raw.append(1)
            else:
                raw.append(0)
        res.append(raw)
    return (count, res)


res = build_map()
v_left = build_visable_map_left(res[0])
v_right = build_visable_map_right(res[0])
v_top = build_visable_map_top(res[0])
v_buttom = build_visable_map_buttom(res[0])
res = count_visable((v_left, v_right, v_top, v_buttom))
print(res[0])
