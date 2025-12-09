d = None
with open("d9.txt", 'r') as f:
    d = [tuple(map(int, reversed(x.strip().split(','))))
         for x in f.readlines()]

d1 = []
for i in range(len(d)):
    x = d[i]
    for j in range(i):
        y = d[j]
        d1.append([x, y, (abs(x[0] - y[0]) + 1) * (abs(x[1] - y[1]) + 1)])

d1.sort(key=lambda x: x[2], reverse=True)

d2 = [(d[i-1], d[i]) for i in range(0, len(d))]

for x in d1:
    x1, y1 = x[0]
    x2, y2 = x[1]
    c = True
    for y in d2:
        left = max(x1, x2) <= min(y[0][0], y[1][0])
        right = min(x1, x2) >= max(y[0][0], y[1][0])
        top = max(y1, y2) <= min(y[0][1], y[1][1])
        bottom = min(y1, y2) >= max(y[0][1], y[1][1])

        if not (left or right or top or bottom):
            c = False
            break

    if c:
        print(x[2])
        break
