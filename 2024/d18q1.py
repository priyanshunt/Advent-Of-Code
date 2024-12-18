d = None
with open("d18q1.txt") as f:
    d = f.read().split('\n')

m = 71
ini = 1024

data = [['.' for i in range(m)] for j in range(m)]

for x in d[:ini]:
    i, j = map(int, x.split(','))
    data[i][j] = '#'

reached = []
to_visit = [((0, 0), 0)]
c = None

while len(to_visit) > 0:
    pos, cost = to_visit.pop(0)
    i, j = pos

    if pos not in reached and 0 <= i < m and 0 <= j < m and data[i][j] == '.':
        reached.append(pos)

        if pos == (m - 1, m - 1):
            c = cost
            break
        else:
            to_visit.append(((i, j + 1), cost + 1))
            to_visit.append(((i, j - 1), cost + 1))
            to_visit.append(((i + 1, j), cost + 1))
            to_visit.append(((i - 1, j), cost + 1))

print(cost)
