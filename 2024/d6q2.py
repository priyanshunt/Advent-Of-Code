d = None
with open("d6q1.txt") as f:
    d = f.read().split('\n')

data = [list(x) for x in d]

l = len(data)
l1 = len(data[0])

pos = None
arrow = None
for i in range(l):
    for j in range(l1):
        if data[i][j] != '.' and data[i][j] != '#':
            pos = (i, j)
            arrow = data[i][j]
            data[i][j] = '.'

ini_pos = pos
ini_arrow = arrow

v = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
r = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

def func(pos, arrow, obs):
    visited = []
    data[obs[0]][obs[1]] = '#'
    t = 0
    
    while(True):
        if (pos, arrow) in visited:
            t = 1
            break
        else:
            visited.append((pos, arrow))
        
        new_pos = (pos[0] + v[arrow][0], pos[1] + v[arrow][1])
        
        if new_pos[0] >= l or new_pos[1] >= l1 or new_pos[0] < 0 or new_pos[1] < 0:
            break
        elif data[new_pos[0]][new_pos[1]] == '#':
            arrow = r[arrow]
        else:
            pos = new_pos
    
    data[obs[0]][obs[1]] = '.'
    return t

un = set()
while(True):
    if pos != ini_pos:
        if func(ini_pos, ini_arrow, pos):
            un.add(pos)
    new_pos = (pos[0] + v[arrow][0], pos[1] + v[arrow][1])
    if new_pos[0] >= l or new_pos[1] >= l1 or new_pos[0] < 0 or new_pos[1] < 0:
        break
    elif data[new_pos[0]][new_pos[1]] == '#':
        arrow = r[arrow]
    else:
        pos = new_pos
print(len(un))
