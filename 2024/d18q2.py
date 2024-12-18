import sys
sys.setrecursionlimit(10 ** 6)

d = None
with open("d18q1.txt") as f:
    d = f.read().split('\n')

m = 71
ini = 1024

data = [['.' for i in range(m)] for j in range(m)]

for x in d[:ini]:
    i, j = map(int, x.split(','))
    data[i][j] = '#'

def func():
    reached = []
    to_visit = [((0, 0), [])]
    best_visited = None
    
    while len(to_visit) > 0:
        pos, visited = to_visit.pop(0)
        i, j = pos

        if pos not in reached and 0 <= i < m and 0 <= j < m and data[i][j] == '.':
            reached.append(pos)
            visited.append(pos)

            if pos == (m - 1, m - 1):
                best_visited = visited
                break
            else:
                to_visit.append(((i, j + 1), visited.copy()))
                to_visit.append(((i, j - 1), visited.copy()))
                to_visit.append(((i + 1, j), visited.copy()))
                to_visit.append(((i - 1, j), visited.copy()))
    
    return best_visited

while True:

    visited = func()

    if visited is None:
        print(d[ini])
        break
    else:
        while True:
            i, j = map(int, d[ini].split(','))
            data[i][j] = '#'
            if (i, j) in visited:
                break
            ini += 1
