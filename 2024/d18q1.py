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

reached = []
ver_cost = {}
def func(pos, visited, cost):
    i, j = pos
    if 0 <= i < m and 0 <= j < m and data[i][j] == '.' and pos not in visited and (pos not in ver_cost or ver_cost[pos] > cost):
        visited.append(pos)
        ver_cost[pos] = cost
        if pos == (m - 1, m - 1):
            reached.append(visited)
        else:
            func((i, j + 1), visited.copy(), cost + 1)
            func((i, j - 1), visited.copy(), cost + 1)
            func((i + 1, j), visited.copy(), cost + 1)
            func((i - 1, j), visited.copy(), cost + 1)

func((0, 0), [], 0)

print(min([len(x) for x in reached]) - 1)
