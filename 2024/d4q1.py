d = None
with open("d4q1.txt") as f:
    d = f.read().split('\n')

data = [list(x) for x in d]

l = len(data)
l1 = len(data[0])
c = 0
m = [[0, 1],[1, 0],[0, -1],[-1, 0],[1, 1],[1, -1],[-1, 1],[-1, -1]]

for i in range(l):
    for j in range(l1):
        for k in m:
            if i + k[0] * 3 >= 0 and i + k[0] * 3 < l and j + k[1] * 3 >= 0 and j + k[1] * 3 < l1:
                word = data[i][j] + data[i+k[0]][j+k[1]] + data[i+k[0]*2][j+k[1] * 2] + data[i+k[0]*3][j+k[1]*3]
                if word == 'XMAS':
                    c += 1

print(c)