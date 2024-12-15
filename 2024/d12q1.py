d = None
with open("d12q1.txt") as f:
    d = f.read().split('\n')

data = [list(x) for x in d]

l = len(data)
l1 = len(data[0])

v = []

def func(pos):
    if pos in v:
        return 0
    else:
        v.append(pos)
        t = 0
        r = 0
        
        i, j = pos
        
        if i - 1 < 0 or data[i - 1][j] != data[i][j]:
            t += 1
        elif data[i - 1][j] == data[i][j]:
            r += func((i - 1, j))
        
        if i + 1 >= l or data[i + 1][j] != data[i][j]:
            t += 1
        elif data[i + 1][j] == data[i][j]:
            r += func((i + 1, j))
        
        if j - 1 < 0 or data[i][j - 1] != data[i][j]:
            t += 1
        elif data[i][j - 1] == data[i][j]:
            r += func((i, j - 1))
        
        if j + 1 >= l1 or data[i][j + 1] != data[i][j]:
            t += 1
        elif data[i][j + 1] == data[i][j]:
            r += func((i, j + 1))
        
        return r + t

s = 0
for i in range(l):
    for j in range(l1):
        pos = (i, j)
        if pos not in v:
            prev = len(v)
            per = func(pos) 
            next = len(v)
            s += per * (next - prev)

print(s)        