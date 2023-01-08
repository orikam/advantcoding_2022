with open('data.txt') as f:
    line = f.readline()
    priority = 0
    sum = 0
    while line:
        l = len(line)
        p1 = line[:l // 2]
        p2 = line[l // 2:]
        res = list(set(p1).intersection(p2))
        if res[0] >= 'a':
            priority = ord(res[0]) - ord('a') + 1
        else:
            priority = ord(res[0]) - ord('A') + 27
        sum += priority
        print(priority)
        line = f.readline()

    print(f'total = {sum}')
