d = None
with open("d16q1.txt") as f:
    d = f.read().split('\n')

data = [list(x) for x in d]
l = len(data)
l1 = len(data[0])

arrow = {'>' : ((0, 1), '^', 'v'), '<' : ((0, -1), '^', 'v'), '^' : ((1, 0), '>', '<'), 'v' : ((-1, 0), '>', '<')}

pos = None
end_pos = None
for i in range(l):
    for j in range(l1):
        if data[i][j] == 'S':
            pos = (i, j)
        if data[i][j] == 'E':
            end_pos = (i, j)


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
                visit_cost[(x[0], x[1])] = x[2]
                score.append(x[2])
            elif data[x[0][0]][x[0][1]] == 'S' or data[x[0][0]][x[0][1]] == '.':
                to_visit.append(x)
                visit_cost[(x[0], x[1])] = x[2]
        else:
            if x[2] < visit_cost[(x[0], x[1])]:
                if data[x[0][0]][x[0][1]] == 'E':
                    visit_cost[(x[0], x[1])] = x[2]
                    score.append(x[2])
                elif data[x[0][0]][x[0][1]] == 'S' or data[x[0][0]][x[0][1]] == '.':
                    to_visit.append(x)
                    visit_cost[(x[0], x[1])] = x[2]     

to_visit = None
for k, v in visit_cost.items():
    if k[0] == end_pos and v == min(score):
        to_visit = [(k[0], k[1], v)]

visited = []
c = 1
d = {'>' : (0, -1), '<' : (0, 1), '^' : (-1, 0), 'v' : (1, 0)}

while len(to_visit) > 0:
    ele = to_visit.pop(0)
    pos, a, cost = ele
    i, j = pos

    if ele not in visited :
        visited.append(ele)
                
        x = d[a]
        i1, j1 = i + x[0], j + x[1]
        new_pos = (i1, j1)
        new_ele_list = [(new_pos, '>'), (new_pos, '<'), (new_pos, 'v'), (new_pos, '^')]
        for new_ele in new_ele_list:

            if new_ele in visit_cost and visit_cost[new_ele] == cost - 1001 and new_ele[1] != a:
                to_visit.append((new_ele[0], new_ele[1], cost - 1001))
            if new_ele in visit_cost and visit_cost[new_ele] == cost - 1 and new_ele[1] == a:
                to_visit.append((new_ele[0], new_ele[1], cost - 1))

pos_list = set()

for x in visited:
    pos_list.add(x[0])

print(len(pos_list))
