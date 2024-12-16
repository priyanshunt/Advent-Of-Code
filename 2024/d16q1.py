import sys

sys.setrecursionlimit(10 ** 6)
INT_MAX = 99999999

d = None
with open("d6p1.txt") as f:
    d = f.read().split('\n')

data = [list(x) for x in d]
l = len(data)
l1 = len(data[0])

arrow = {'>' : ((0, 1), '^', 'v'), '<' : ((0, -1), '^', 'v'), '^' : ((1, 0), '>', '<'), 'v' : ((-1, 0), '>', '<')}

visited = {}
def func(pos, a, li, cost):
    li.append((pos, a))
    i, j = pos
    a1 = arrow[a]
    i1, j1 = a1[0]
    new_pos = (i + i1, j + j1)
    # print(pos, a)
    if (pos, a) not in visited or cost :
        visited[(pos, a)] = 9999999
        c = None
        if data[i][j] == 'E':
            c = 1
            print(li)
        elif data[i][j] == '.' or data[i][j] == 'S':
            c = min(1 + func(new_pos, a, li.copy()), 1000 + func(pos, a1[1], li.copy()), 1000 + func(pos, a1[2], li.copy()))
        else:
            c = INT_MAX
        if (pos, a) not in visited or c < visited[(pos, a)]:
            visited[(pos, a)] = c
            return c
        else:
            return visited[(pos, a)]
    else:
        return visited[(pos, a)]
    

pos = None
for i in range(l):
    for j in range(l1):
        if data[i][j] == 'S':
            pos = (i, j)

s = func(pos, '>', [], INT_MAX)

print(s)
