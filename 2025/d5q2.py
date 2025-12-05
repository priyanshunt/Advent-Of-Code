d = None
with open("d5.txt", 'r') as f:
    d = [x.strip() for x in f.readlines()]

i = d.index('')
d = d[:i]
d = [list(map(int, x.split('-'))) for x in d]
d.sort(key=lambda x: x[0])

l = [d[0]]
for x in d[1:]:
    if l[-1][1] >= x[0] and l[-1][1] <= x[1]:
        l[-1][1] = x[1]
    elif l[-1][1] < x[0]:
        l.append(x)

s = 0
for x in l:
    s += x[1] - x[0] + 1

print(s)
