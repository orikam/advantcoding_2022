with open('data.txt') as f:
    line = f.readline()
    res = 0
    l = []
    while line:
        #print(l)    
        if line =="\n":
            print('enter')
            l.append(res)
            res = 0
        else:
            value = int(line)
            res += value
        line = f.readline()
    total = 0
    for x in range(3):
        m = max(l)
        total += m
        l.remove(m)

    #print(f'{l.index(m)} - {m}')
    print(f'total {total}')