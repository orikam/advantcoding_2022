
def build_map():
    map = []
    with open('data.txt') as f:
        line = f.readline()
        line = line[:-1]
        line = [int(x) for x in line]
        while line:
            map.append(list(line))
            line = f.readline()
            line = line[:-1]
            line = [int(x) for x in line]
    return (map, len(map), len(map[0]))   

def build_max_map_left(map):
    max_map = []
    for j in range(len(map)):
        max = 0
        raw = []
        raw.append(max)
        for i in range(len(map[0]) - 1):
            if map[j][i] > max:
                max = map[j][i]
            raw.append(max)
        max_map.append(raw)
    return max_map

def build_max_map_right(map):
    max_map = []
    for j in range(len(map)):
        max = 0
        raw = []
        raw.append(max)
        for i in range(len(map[0]) - 1, 0, -1):
            if map[j][i] > max:
                max = map[j][i]
            raw.insert(0, max)
        max_map.append(raw)
    return max_map
    
res = build_map()
max_left = build_max_map_right(res[0])
print(max_left)