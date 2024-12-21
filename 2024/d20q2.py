d = None
with open("d20q1.txt") as f:
    d = f.read().split('\n')

data = [list(x) for x in d]

l = len(data)
l1 = len(data[0])

start_pos = None
end_pos = None
for i in range(l):
    for j in range(l1):
        if data[i][j] == 'S':
            start_pos = (i, j)
        if data[i][j] == 'E':
            end_pos = (i, j)

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

reached = []
pos = start_pos
while pos:
    reached.append(pos)
    i, j = pos

    for x in d:
        i1, j1 = i + x[0], j + x[1]
        new_pos = (i1, j1)

        if 1 <= i1 < l - 1 and 1 <= j1 < l1 - 1 and new_pos not in reached:
            if data[i1][j1] == '.':
                pos = new_pos
            elif data[i1][j1] == 'E':
                reached.append(new_pos)
                pos = None

dist = reached.index(end_pos)
reached_r = reached[::-1]

s = 0
for x in range(dist):
    for y in range(dist):
        
        i, j = reached[x]
        i1, j1 = reached_r[y]

        if 0 < abs(i - i1) + abs(j - j1) <= 20:
            if x + abs(i - i1) + abs(j - j1) + y <= dist - 100:
                s += 1

print(s)