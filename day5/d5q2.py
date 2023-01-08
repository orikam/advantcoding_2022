
map = [['R','S','L','F','Q'],
       ['N', 'Z', 'Q','G','P','T'],
       ['S','M','Q','B'],
       ['T','G','Z','J','H','C','B','Q'],
       ['P','H','M','B','N','F','S'],
       ['P','C','Q','N','S','L','V','G'],
       ['W','C','F'],
       ['Q','H','G','Z','W','V','P','M'],
       ['G','Z','D','L','C','N','R']]
map1 = [['Z','N'],
        ['M','C','D'],
        ['P']]
#map = map1
with open('data.txt') as f:
    line = f.readline()
    while line:
        temp = line.split()
        data = [int(x) for x in temp if x.isdigit()]
        map[data[2]-1] += map[data[1]-1][-data[0]:]
        map[data[1]-1] = map[data[1]-1][:-data[0]]
        
        line = f.readline()
for x in map:
    print(x.pop(), end ="")
