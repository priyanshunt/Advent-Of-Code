d = None
with open("d16q1.txt") as f:
    d = f.read().split('\n')

data = [list(x) for x in d]
l = len(data)
l1 = len(data[0])

arrow = {'>' : ((0, 1), '^', 'v'), '<' : ((0, -1), '^', 'v'), '^' : ((1, 0), '>', '<'), 'v' : ((-1, 0), '>', '<')}

pos = None
for i in range(l):
    for j in range(l1):
        if data[i][j] == 'S':
            pos = (i, j)


visit_cost = {(pos, '>') : 0}
to_visit = [(pos, '>', 0)]
score = []

while len(to_visit) > 0:
    ele = to_visit.pop(0)
    pos, a, cost = ele
    i, j = pos
    
    a1 = arrow[a]
    i1, j1 = a1[0]
    a2 = a1[1]
    a3 = a1[2]

    new_ele = [((i + i1, j + j1), a, cost + 1), (pos, a2, cost + 1000), (pos, a3, cost + 1000)]

    for x in new_ele:
        if (x[0], x[1]) not in visit_cost:
            if data[x[0][0]][x[0][1]] == 'E':
                score.append(x[2])
            elif data[x[0][0]][x[0][1]] == 'S' or data[x[0][0]][x[0][1]] == '.':
                to_visit.append(x)
                visit_cost[(x[0], x[1])] = x[2]
        else:
            if (data[x[0][0]][x[0][1]] == 'S' or data[x[0][0]][x[0][1]] == '.') and x[2] < visit_cost[(x[0], x[1])]:
                to_visit.append(x)
                visit_cost[(x[0], x[1])] = x[2]

print(min(score))
