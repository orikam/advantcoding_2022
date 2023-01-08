
memory_size = 70000000
target_memory = memory_size - 30000000

class dir():
    def __init__(self) -> None:
        self.dirs = {}
        self.files = []
        self.total = 0
        self.parent = None
    
    def __str__(self) -> str:
        dirs_text = 'Total = ' + str(self.total) + ' '
        for d in self.dirs.items():
            dirs_text += str(d[0])+ '[' + str(d[1]) + ']' + ','
        for d in self.files:
            dirs_text += str(d) + ','
        return f'{dirs_text}'
    
    def calc_size(self) -> int: 
        self.total = 0
        for f in self.files:
            self.total += int(f[0])
        for d in self.dirs.values():
            self.total += d.calc_size()
        return self.total

    def get_size(self, limit):
        res = 0
        for d in self.dirs.values():
            res += d.get_size(limit)
        if self.total <= limit:
            res += self.total
        return res
    
    def find_space(self, size, target, current_value):
        value = target - (size - self.total)
        res = 0
        if value > 0 and value < current_value:
            res = self.total
            for f in self.dirs.values():
                temp = f.find_space(size, target, current_value)
                if temp < res:
                    res = temp
        else:
            res = size
        return res

root = dir()

state = root
with open('data.txt') as f:
    line = f.readline()
    while line:
        data = line.split()
        if data[0] == '$':
            if data[1] == 'cd':
                if data[2] == '/':
                    state = root
                elif data[2] == '..':
                    state = state.parent
                else:
                    state = state.dirs[data[2]]
            elif data[1] == 'ls':
                pass
        elif data[0].isdigit():
            state.total += int(data[0])
            state.files.append((data[0], data[1]))
        elif data[0] == 'dir':
            s = dir()
            s.parent = state
            state.dirs[data[1]] = s
        line = f.readline()
    print(str(root))
    print('-----')
    size = root.calc_size()
    ans = root.get_size(100000)
    
    space = root.find_space(size, target_memory, size)
    print(f'the result is {size} the ans is {ans}, space {space}')