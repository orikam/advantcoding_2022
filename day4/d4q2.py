with open('data.txt') as f:
    line = f.readline()
    sum = 0
    while line:
        temp = line.split(',')
        data = temp[0].split('-')
        data += temp[1].split('-')
        data1 = [int(x) for x in data]
        if data1[0] > data1[3] or data1[1] < data1[2]:
            pass
        else:
            sum +=1
        line = f.readline()
    print(sum)