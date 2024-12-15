d = None
with open("d8q1.txt") as f:
    d = f.read().split('\n')

data = [list(x) for x in d]

l = len(data)
l1 = len(data[0])
points = {}

for i in range(l):
    for j in range(l1):
        x = data[i][j]
        if x.isalnum():
            if x in points:
                points[x].append((i , j))
            else:
                points[x] = [(i, j)]

valid = 0

for v in points.values():
    lv = len(v)
    for i in range(lv - 1):
        for j in range(i+1, lv):
            x1, y1 = v[i]
            x2, y2 = v[j]
            
            t = 2
            while(True):
                x3, y3 = t * x1 - (t - 1) * x2, t * y1 - (t - 1) * y2
                if 0 <= x3 < l and 0 <= y3 < l1:
                    if data[x3][y3] == '.':
                        valid += 1
                        data[x3][y3] = '#'
                else:
                    break
                t += 1

            t = 2
            while(True):
                x4, y4 = t * x2 - (t - 1) * x1, t * y2 - (t - 1) * y1
                if 0 <= x4 < l and 0 <= y4 < l1:
                    if data[x4][y4] == '.':
                        valid += 1
                        data[x4][y4] = '#'
                else:
                    break
                t += 1

print(valid + sum([len(v) for v in points.values()]))