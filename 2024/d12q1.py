d = None
with open("d12q1.txt") as f:
    d = f.read().split('\n')

data = [list(x) for x in d]

l = len(data)
l1 = len(data[0])

v = []
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def func(pos):
    if pos in v:
        return 0
    else:
        v.append(pos)
        t = 0
        r = 0
        
        i, j = pos
        
        for x in d:
            m = x[0]
            m1 = x[1]
            if 0 <= i + m < l and 0 <= j + m1 < l1:
                if data[i + m][j + m1] != data[i][j]:
                    t += 1
                else:
                    r += func((i + m, j + m1))
            else:
                t += 1
        return r + t

s = 0
for i in range(l):
    for j in range(l1):
        pos = (i, j)
        if pos not in v:
            prev = len(v)
            peri = func(pos) 
            next = len(v)
            s += peri * (next - prev)

print(s)
