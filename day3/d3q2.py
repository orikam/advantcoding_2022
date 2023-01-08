with open('data.txt') as f:
    line = f.readline()
    priority = 0
    sum = 0
    state = 0
    while line:
        line = line[:-1]
        if state % 3 == 0:
            l = line
        elif state % 3 == 1:
            shared = list(set(l).intersection(line))
        elif state %3 == 2:
            res = list(set(shared).intersection(line))
            if res[0] >= 'a':
                priority = ord(res[0]) - ord('a') + 1
            else:
                priority = ord(res[0]) - ord('A') + 27
            sum += priority
            print(priority)
        state += 1
        line = f.readline()

    print(f'total = {sum}')
