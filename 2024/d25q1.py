d = None
with open("d25q1.txt") as f:
    d = f.read().split('\n\n')

lock = []
key = []

for x in d:
    y = x.split('\n')
    l = [0 for _ in range(len(y[0]))]
    for z in y[1:-1]:
        for i in range(len(z)):
            if z[i] == '#':
                l[i] += 1
    if y[0][0] == '#':
        lock.append(l)
    else:
        key.append(l)

s = 0
for x in lock:
    for y in key:
        if all(i + j <= 5 for i, j in zip(x, y)):
            s += 1
print(s)
