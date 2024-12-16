d = None
with open("d12q1.txt") as f:
    d = f.read().split('\n')

data = [list(x) for x in d]

l = len(data)
l1 = len(data[0])

v = []
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
corner = [[(-1, 0), (0, -1)], [(-1, 0), (0, 1)], [(1, 0), (0, 1)], [(1, 0), (0, -1)]]

def func(pos):
    if pos in v:
        return 0
    else:
        v.append(pos)
        t = 0
        r = 0
        
        i, j = pos
        
        for x in corner:
            pos1 = (pos[0] + x[0][0], pos[1] + x[0][1])
            pos2 = (pos[0] + x[1][0], pos[1] + x[1][1])
            pos3 = (pos[0] + x[0][0] + x[1][0], pos[1] + x[0][1] + x[1][1])
            if (pos1[0] < 0 or pos1[0] >= l or pos1[1] < 0 or pos1[1] >= l1 or data[pos1[0]][pos1[1]] != data[i][j]) and (pos2[0] < 0 or pos2[0] >= l or pos2[1] < 0 or pos2[1] >= l1 or data[pos2[0]][pos2[1]] != data[i][j]):
                t += 1
            elif 0 <= pos1[0] < l and 0 <= pos1[1] < l1 and data[pos1[0]][pos1[1]] == data[i][j] and 0 <= pos2[0] < l and 0 <= pos2[1] < l1 and data[pos2[0]][pos2[1]] == data[i][j] and data[pos3[0]][pos3[1]] != data[i][j]:
                t += 1

        for x in d:
            m, m1 = x
            if 0 <= i + m < l and 0 <= j + m1 < l1 and data[i + m][j + m1] == data[i][j]:
                r += func((i + m, j + m1))          

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
