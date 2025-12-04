d = None
with open("d4.txt", 'r') as f:
    d = [list(x.strip()) for x in f.readlines()]

d1 = [(-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1), (0, 1), (1, 0), (1, 1)]

s = 0
for i in range(len(d)):
    for j in range(len(d[i])):
        if d[i][j] == '@':
            c = 0
            for z in d1:
                x, y = z
                if x + i >= 0 and x + i < len(d) and y + j >= 0 and y + j < len(d[i]) and d[x+i][y+j] == '@':
                    c += 1
            if c < 4:
                s += 1

print(s)
