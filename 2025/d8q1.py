import math

d = None
with open("d8.txt", 'r') as f:
    d = [list(map(int, x.strip().split(','))) for x in f.readlines()]

d1 = {}

for i in range(len(d)):
    for j in range(i):
        d1[(i, j)] = math.dist(d[i], d[j])

d1 = dict(sorted(d1.items(), key=lambda x: x[1]))

s = []
j = 0

for k, v in d1.items():
    if j == 1000:
        break
    j += 1
    x, y = k
    xi = None
    yi = None
    for i in range(len(s)):
        if x in s[i]:
            xi = i
        if y in s[i]:
            yi = i
        if xi is not None and yi is not None:
            break
    if yi is None:
        if xi is None:
            s.append([x, y])
        else:
            s[xi].append(y)
    else:
        if xi is None:
            s[yi].append(x)
        else:
            if xi != yi:
                s[xi] += s[yi]
                s.pop(yi)

s.sort(key=lambda x: len(x))

p = 1
for x in s[-3:]:
    p *= len(x)

print(p)
