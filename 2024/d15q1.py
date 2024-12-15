d = None
with open("d15q1.txt") as f:
    d = f.read().split('\n')

t = 0
data = [[], []]
for x in d:
    if x == '':
        t = 1
        continue
    data[t].append(x)

m = ''.join(data[1])
data= [list(x) for x in data[0]]

l = len(data)
l1 = len(data[0])

pos = None
for i in range(l):
    for j in range(l1):
        if data[i][j] == '@':
            pos = (i, j)
            break

d = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

for x in m:
    y = d[x]
    pos1 = (pos[0] + y[0], pos[1] + y[1])
    
    move_pos = [pos]
    move_ele = ['@']
    t = 0
    while data[pos1[0]][pos1[1]] != '#':
        move_pos.append(pos1)
        if data[pos1[0]][pos1[1]] == '.':
            move_ele.insert(0, '.')
            pos = move_pos[1]
            break
        else:
            move_ele.append(data[pos1[0]][pos1[1]])
            pos1 = (pos1[0] + y[0], pos1[1] + y[1])
            
    for p, e in zip(move_pos, move_ele):
        data[p[0]][p[1]] = e

s = 0
for i in range(l):
    for j in range(l1):
        if data[i][j] == 'O':
            s += 100 * i + j
print(s)